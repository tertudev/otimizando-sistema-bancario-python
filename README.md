# 🏦 Sistema Bancário em Python

Este é um projeto simples desenvolvido em **Python**, que simula um sistema bancário básico. O objetivo foi praticar os fundamentos da linguagem, como variáveis, condicionais, loops e entradas do usuário.

## 🔹 Funcionalidades

O sistema permite ao usuário:

1. **Depositar** valores na conta.
2. **Sacar** valores respeitando limite de saque diário e saldo disponível.
3. Consultar o **extrato**, exibindo todas as movimentações.
4. **Sair** do sistema de forma segura.

## 🔹 Regras Implementadas

- O usuário possui um **limite de saque diário** de 3 transações.
- O valor máximo permitido por saque é **R$ 500**.
- Não é permitido depositar ou sacar valores negativos.
- O extrato exibe todas as movimentações realizadas (depósitos e saques).

## 🔹 Tecnologias e Conceitos Usados

- Linguagem: **Python 3**
- Conceitos aplicados:
  - Variáveis
  - Operadores aritméticos
  - Estruturas de decisão: `if`, `elif`, `else`
  - Loops: `while`
  - Entrada de dados com `input()`
  - Saída de dados com `print()`
  - Strings e concatenação

## 🔹 Como Usar

1. Clone ou faça download do arquivo `sistema_bancario.py`.
2. Execute o arquivo no terminal ou em um ambiente Python.
3. Siga as instruções do menu para realizar depósitos, saques ou consultar o extrato.
4. Para sair, escolha a opção `q`.

## 🔹 Estrutura do Código

O código é simples e organizado da seguinte forma:

- Inicialização de variáveis: `saldo`, `extrato`, `saques`, etc.
- Loop principal com o menu de opções.
- Condicionais para cada operação:
  - **Depósito**: verifica se o valor é válido e atualiza saldo e extrato.
  - **Saque**: verifica saldo, limite por saque e limite de saques diários antes de permitir a operação.
  - **Extrato**: exibe todas as movimentações ou mensagem caso não haja nenhuma.
  - **Sair**: encerra o programa.

## 🔹 Aprendizados

Com este projeto, pude:

- Praticar a lógica de programação com Python.
- Entender melhor o fluxo de um sistema bancário simples.
- Aplicar conceitos básicos de controle de fluxo, entrada e saída de dados.
- Criar um projeto funcional que pode ser expandido no futuro (ex: adicionando contas, autenticação, histórico de transações mais detalhado, etc.).

Vamos codar o futuro! 🚀
