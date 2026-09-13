# CONTEXT_RULES.md

## Objetivo

Este documento define as regras obrigatórias para o desenvolvimento do TaskAnalyzer com auxílio de Inteligência Artificial.

## Diretrizes arquiteturais

1. Utilizar Python 3.11 ou superior.
2. Utilizar type hints em funções e métodos.
3. Seguir o princípio Single Responsibility Principle (SRP).
4. Seguir as boas práticas da PEP 8.
5. Utilizar Google Style Docstrings.
6. Manter as funções pequenas e com responsabilidade única.
7. Utilizar tratamento específico de exceções.
8. Utilizar mensagens de erro claras.
9. Utilizar o módulo logging para registros.
10. Utilizar nomes de variáveis e funções descritivos.
11. Manter o código legível, simples e sustentável.
12. Toda nova funcionalidade deve possuir testes correspondentes.

## Proibições

1. Não utilizar bibliotecas externas não autorizadas.
2. Não alterar os cenários de teste definidos na especificação.
3. Não modificar a estrutura de pastas definida no projeto.
4. Não persistir dados em arquivos ou bancos de dados.
5. Não alterar a assinatura das funções públicas sem autorização.
6. Não gerar código sem testes correspondentes.
7. Não inserir código duplicado ou desnecessário.
8. Não assumir comportamentos que não estejam definidos na especificação.
9. Não ignorar as regras de validação.
10. Não remover testes existentes para fazer o código passar.

## Regra principal

A especificação técnica, o contrato de negócio e os cenários de aceite são a fonte de verdade do projeto.

Qualquer comportamento não especificado deverá ser identificado antes de ser implementado.
