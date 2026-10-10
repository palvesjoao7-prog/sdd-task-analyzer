
"""Implementação do sistema TaskAnalyzer."""

from datetime import datetime
from typing import Any


class TaskValidationError(ValueError):
    """Erro lançado quando os dados de uma tarefa são inválidos."""


def analyze_tasks(tasks: list[dict[str, Any]]) -> dict[str, Any]:
    """Analisa tarefas e retorna métricas de produtividade."""

    if not isinstance(tasks, list):
        raise TaskValidationError("A entrada deve ser uma lista de tarefas.")

    priorities = {"baixa", "média", "alta"}
    statuses = {"pendente", "concluída", "cancelada"}

    ids: set[str] = set()
    completed_times: list[float] = []
    analyzed_tasks = 0
    completed_count = 0
    overdue_count = 0

    by_priority: dict[str, dict[str, int]] = {
        priority: {
            "total": 0,
            "concluidas": 0,
            "pendentes": 0,
            "canceladas": 0,
            "atrasadas": 0,
        }
        for priority in priorities
    }

    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise TaskValidationError(
                f"A tarefa na posição {index} deve ser um dicionário."
            )

        required = {
            "id", "titulo", "prioridade",
            "data_criacao", "prazo", "status",
        }

        missing = required - task.keys()
        if missing:
            raise TaskValidationError(
                f"Tarefa {index}: campos obrigatórios ausentes: "
                f"{', '.join(sorted(missing))}."
            )

        task_id = task["id"]
        title = task["titulo"]
        priority = task["prioridade"]
        created = task["data_criacao"]
        deadline = task["prazo"]
        status = task["status"]
        finished = task.get("data_conclusao")

        if not isinstance(task_id, str) or not task_id.strip():
            raise TaskValidationError("O id deve ser um texto não vazio.")
        if task_id in ids:
            raise TaskValidationError(f"ID duplicado: {task_id}.")
        ids.add(task_id)

        if not isinstance(title, str) or not title.strip():
            raise TaskValidationError("O título deve ser um texto não vazio.")
        if priority not in priorities:
            raise TaskValidationError(f"Prioridade inválida: {priority}.")
        if status not in statuses:
            raise TaskValidationError(f"Status inválido: {status}.")

        if not isinstance(created, datetime) or not isinstance(deadline, datetime):
            raise TaskValidationError(
                "Data de criação e prazo devem ser objetos datetime."
            )

        if finished is not None and not isinstance(finished, datetime):
            raise TaskValidationError(
                "A data de conclusão deve ser datetime ou None."
            )

        if created.tzinfo != deadline.tzinfo:
            raise TaskValidationError(
                "As datas de criação e prazo devem usar fusos compatíveis."
            )

        if finished is not None and finished.tzinfo != created.tzinfo:
            raise TaskValidationError(
                "A data de conclusão deve usar fuso compatível."
            )

        if created > deadline:
            raise TaskValidationError(
                "A data de criação não pode ser posterior ao prazo."
            )

        if status == "concluída" and finished is None:
            raise TaskValidationError(
                "Tarefas concluídas precisam de data de conclusão."
            )

        if status != "concluída" and finished is not None:
            raise TaskValidationError(
                "Somente tarefas concluídas podem ter data de conclusão."
            )

        if finished is not None and finished < created:
            raise TaskValidationError(
                "A data de conclusão não pode anteceder a criação."
            )

        analyzed_tasks += 1
        metrics = by_priority[priority]
        metrics["total"] += 1

        if status == "concluída":
            completed_count += 1
            metrics["concluidas"] += 1
            assert finished is not None
            completed_times.append((finished - created).total_seconds() / 3600)

            if finished > deadline:
                overdue_count += 1
                metrics["atrasadas"] += 1

        elif status == "pendente":
            metrics["pendentes"] += 1
        else:
            metrics["canceladas"] += 1

    average_time = (
        sum(completed_times) / len(completed_times)
        if completed_times else 0.0
    )
    delay_rate = (
        overdue_count / completed_count * 100
        if completed_count else 0.0
    )

    return {
        "quantidade_analisada": analyzed_tasks,
        "quantidade_concluida": completed_count,
        "quantidade_atrasada": overdue_count,
        "tempo_medio_conclusao_horas": average_time,
        "taxa_atraso_percentual": delay_rate,
        "por_prioridade": by_priority,
    }
