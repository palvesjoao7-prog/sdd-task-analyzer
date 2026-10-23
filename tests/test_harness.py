
"""Testes automatizados do sistema TaskAnalyzer."""

from datetime import datetime, timedelta

import pytest

from src.task_analyzer import TaskValidationError, analyze_tasks


def criar_tarefa(
    identificador: str,
    status: str = "concluída",
    prioridade: str = "alta",
    dias_para_concluir: int = 1,
    atraso_dias: int = 0,
) -> dict:
    """Cria uma tarefa de exemplo para os testes."""
    criacao = datetime(2026, 1, 1, 9, 0)
    prazo = criacao + timedelta(days=2)
    conclusao = criacao + timedelta(days=dias_para_concluir, hours=2)

    if atraso_dias:
        conclusao = prazo + timedelta(days=atraso_dias)

    tarefa = {
        "id": identificador,
        "titulo": f"Tarefa {identificador}",
        "prioridade": prioridade,
        "data_criacao": criacao,
        "prazo": prazo,
        "status": status,
    }

    if status == "concluída":
        tarefa["data_conclusao"] = conclusao

    return tarefa


def test_lista_vazia():
    resultado = analyze_tasks([])

    assert resultado["quantidade_analisada"] == 0
    assert resultado["quantidade_concluida"] == 0
    assert resultado["quantidade_atrasada"] == 0
    assert resultado["tempo_medio_conclusao_horas"] == 0
    assert resultado["taxa_atraso_percentual"] == 0


def test_tarefa_concluida_no_prazo():
    tarefa = criar_tarefa("1", dias_para_concluir=1)

    resultado = analyze_tasks([tarefa])

    assert resultado["quantidade_analisada"] == 1
    assert resultado["quantidade_concluida"] == 1
    assert resultado["quantidade_atrasada"] == 0
    assert resultado["tempo_medio_conclusao_horas"] == 26


def test_tarefa_atrasada():
    tarefa = criar_tarefa("2", atraso_dias=1)

    resultado = analyze_tasks([tarefa])

    assert resultado["quantidade_atrasada"] == 1
    assert resultado["taxa_atraso_percentual"] == 100


def test_tarefa_pendente():
    tarefa = criar_tarefa("3", status="pendente")

    resultado = analyze_tasks([tarefa])

    assert resultado["quantidade_analisada"] == 1
    assert resultado["quantidade_concluida"] == 0
    assert resultado["tempo_medio_conclusao_horas"] == 0


def test_agrupamento_por_prioridade():
    tarefas = [
        criar_tarefa("4", prioridade="alta"),
        criar_tarefa("5", prioridade="baixa"),
        criar_tarefa("6", prioridade="média"),
    ]

    resultado = analyze_tasks(tarefas)
    prioridades = resultado["por_prioridade"]

    assert prioridades["alta"]["total"] == 1
    assert prioridades["baixa"]["total"] == 1
    assert prioridades["média"]["total"] == 1


def test_prioridade_invalida():
    tarefa = criar_tarefa("7", prioridade="urgente")

    with pytest.raises(TaskValidationError, match="Prioridade inválida"):
        analyze_tasks([tarefa])


def test_id_duplicado():
    tarefa1 = criar_tarefa("8")
    tarefa2 = criar_tarefa("8")

    with pytest.raises(TaskValidationError, match="ID duplicado"):
        analyze_tasks([tarefa1, tarefa2])


def test_data_de_conclusao_ausente():
    tarefa = criar_tarefa("9")
    tarefa.pop("data_conclusao")

    with pytest.raises(TaskValidationError, match="data de conclusão"):
        analyze_tasks([tarefa])

def test_tarefa_cancelada_nao_entra_no_tempo_medio():
    tarefa = criar_tarefa("10", status="cancelada")

    resultado = analyze_tasks([tarefa])

    assert resultado["quantidade_analisada"] == 1
    assert resultado["quantidade_concluida"] == 0
    assert resultado["tempo_medio_conclusao_horas"] == 0
    assert resultado["por_prioridade"]["alta"]["canceladas"] == 1


def test_id_vazio():
    tarefa = criar_tarefa("11")
    tarefa["id"] = "   "

    with pytest.raises(TaskValidationError, match="id"):
        analyze_tasks([tarefa])


def test_titulo_vazio():
    tarefa = criar_tarefa("12")
    tarefa["titulo"] = ""

    with pytest.raises(TaskValidationError, match="título"):
        analyze_tasks([tarefa])


def test_data_de_criacao_invalida():
    tarefa = criar_tarefa("13")
    tarefa["data_criacao"] = "2026-01-01"

    with pytest.raises(TaskValidationError, match="datetime"):
        analyze_tasks([tarefa])


def test_data_de_criacao_posterior_ao_prazo():
    tarefa = criar_tarefa("14")
    tarefa["data_criacao"] = tarefa["prazo"] + timedelta(days=1)

    with pytest.raises(TaskValidationError, match="posterior ao prazo"):
        analyze_tasks([tarefa])


def test_data_de_conclusao_anterior_a_criacao():
    tarefa = criar_tarefa("15")
    tarefa["data_conclusao"] = tarefa["data_criacao"] - timedelta(hours=1)

    with pytest.raises(TaskValidationError, match="anteceder a criação"):
        analyze_tasks([tarefa])


def test_status_invalido():
    tarefa = criar_tarefa("16")
    tarefa["status"] = "em andamento"

    with pytest.raises(TaskValidationError, match="Status inválido"):
        analyze_tasks([tarefa])
