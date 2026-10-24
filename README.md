
# TaskAnalyzer

## Descrição

O TaskAnalyzer é um sistema desenvolvido para análise de tarefas e métricas de produtividade, utilizando a abordagem Spec-Driven Development (SDD).

## Objetivo

O sistema tem como objetivo analisar tarefas e calcular métricas de produtividade, incluindo tempo médio de conclusão, taxa de atraso e indicadores por prioridade.

## Funcionalidades

- Análise e validação de tarefas.
- Cálculo do tempo médio de conclusão.
- Cálculo da taxa de atraso.
- Contagem de tarefas concluídas, atrasadas, pendentes e canceladas.
- Agrupamento de métricas por prioridade.
- Tratamento de dados inválidos.
- Registro de informações utilizando o módulo logging.

## Tecnologias

- Python 3.11 ou superior
- pytest
- Git e GitHub
- Inteligência Artificial para desenvolvimento assistido

## Estrutura do projeto

- `README.md` - Documentação geral do projeto.
- `CONTEXT_RULES.md` - Regras de contexto para utilização da Inteligência Artificial.
- `specs/` - Especificação técnica do sistema.
- `tests/` - Testes automatizados.
- `src/` - Código-fonte do sistema.
- `.github/workflows/` - Configuração da integração contínua.

## Instalação

É necessário ter o Python 3.11 ou superior instalado.

Instale o pytest com o comando:

```bash
python -m pip install pytest
```

## Execução dos testes

Na pasta raiz do projeto, execute:

```bash
python -m pytest -v
```

Os testes automatizados verificam o comportamento do sistema, incluindo cálculos de métricas e validações de dados.

## Integração contínua

O projeto utiliza GitHub Actions para executar os testes automatizados conforme a configuração do workflow.

## Autor

João Victor Pereira Alves

## Turma

TURMA A
