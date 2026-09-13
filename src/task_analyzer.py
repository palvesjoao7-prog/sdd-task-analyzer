"""Implementação do sistema TaskAnalyzer."""
# TaskAnalyzer — Especificação Técnica SDD

## 1. Visão Geral

O TaskAnalyzer é um sistema destinado à análise de tarefas e geração de métricas de produtividade.

O sistema recebe um conjunto de tarefas e calcula informações relacionadas ao tempo de conclusão, atrasos e distribuição das tarefas por prioridade.

A especificação técnica funciona como contrato para orientar o desenvolvimento do sistema e a geração de código assistida por Inteligência Artificial.

---

## 2. Propósito do Sistema

O sistema deverá:

- Analisar tarefas executadas.
- Calcular o tempo médio de conclusão.
- Calcular a taxa de atraso.
- Identificar tarefas atrasadas.
- Gerar indicadores por prioridade.
- Validar os dados recebidos.
- Retornar métricas de forma estruturada.

---

## 3. Entradas

Cada tarefa deverá possuir os seguintes dados:

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | str | Sim | Identificador único da tarefa |
| titulo | str | Sim | Título da tarefa |
| prioridade | str | Sim | Prioridade da tarefa |
| data_criacao | datetime | Sim | Data de criação |
| data_conclusao | datetime | Não | Data de conclusão |
| prazo | datetime | Sim | Prazo para conclusão |
| status | str | Sim | Status da tarefa |

### Valores permitidos

**Prioridade:**
- baixa
- média
- alta

**Status:**
- pendente
- concluída
- cancelada

---

## 4. Saídas

O sistema deverá retornar as seguintes métricas:

- tempo médio de conclusão;
- taxa de atraso;
- quantidade de tarefas analisadas;
- quantidade de tarefas concluídas;
- quantidade de tarefas atrasadas;
- indicadores agrupados por prioridade.

As métricas deverão ser retornadas de maneira estruturada e consistente.

---

## 5. Regras de Negócio

1. Apenas tarefas concluídas poderão ser utilizadas no cálculo do tempo médio de conclusão.
2. O tempo de conclusão será calculado pela diferença entre a data de conclusão e a data de criação.
3. Uma tarefa será considerada atrasada quando sua data de conclusão for posterior ao prazo.
4. Tarefas pendentes não deverão ser consideradas concluídas.
5. Tarefas canceladas não deverão ser consideradas no cálculo do tempo médio de conclusão.
6. A taxa de atraso deverá considerar as tarefas aplicáveis à análise.
7. Os indicadores deverão ser organizados por prioridade.
8. Dados inválidos deverão gerar erros específicos e mensagens claras.
9. A divisão por zero deverá ser tratada explicitamente.
10. O sistema não deverá persistir dados em arquivos ou bancos de dados.

---

## 6. Cenários de Aceite

### 6.1 Cenário 1 — Sucesso

**Dado** um conjunto de tarefas válidas com diferentes prioridades, prazos e status,

**Quando** o analisador for executado,

**Então** o sistema deverá retornar corretamente:

- tempo médio de conclusão;
- taxa de atraso;
- quantidade de tarefas concluídas;
- quantidade de tarefas atrasadas;
- indicadores por prioridade.

---

### 6.2 Cenário 2 — Erro

**Dado** uma entrada contendo dados inválidos ou uma situação de divisão por zero,

**Quando** o analisador for executado,

**Então** o sistema deverá gerar uma exceção específica e apresentar uma mensagem clara indicando o problema.

---

## 7. Test Harness

Os cenários definidos nesta especificação deverão ser transformados em testes automatizados utilizando `pytest`.

Os testes deverão verificar:

- processamento de entradas válidas;
- cálculo correto das métricas;
- identificação de tarefas atrasadas;
- agrupamento por prioridade;
- tratamento de entradas inválidas;
- tratamento de divisão por zero.

Os testes deverão funcionar como mecanismo de validação do código gerado por Inteligência Artificial.

---

## 8. Critérios de Validação

O código será considerado válido quando:

1. Respeitar o contrato definido nesta especificação.
2. Passar pelos testes automatizados.
3. Respeitar as regras definidas no arquivo `CONTEXT_RULES.md`.
4. Utilizar Python 3.11 ou superior.
5. Utilizar type hints.
6. Possuir tratamento adequado de exceções.
7. Possuir código legível e organizado.
8. Não implementar comportamentos que não estejam definidos nesta especificação.

---

## 9. Restrições

- Não utilizar bibliotecas externas não autorizadas.
- Não persistir dados em arquivos ou bancos de dados.
- Não alterar a assinatura das funções públicas sem autorização.
- Não modificar os cenários de teste sem autorização.
- Não criar funcionalidades que não estejam especificadas.
- Não inserir código duplicado ou desnecessário.

---

## 10. Objetivo para a Fase 2

Na Fase 2, a especificação será utilizada como base para o desenvolvimento assistido por Inteligência Artificial.

O código deverá ser implementado conforme este contrato e validado pelos testes automatizados.

O desenvolvimento deverá utilizar versionamento com Git e GitHub.
