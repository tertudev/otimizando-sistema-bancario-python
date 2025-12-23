# 🏦 Sistema Bancário Simplificado em Python

Um projeto educacional em Python que simula operações bancárias básicas para demonstrar fundamentos da linguagem.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/github/license/tertudev/otimizando-sistema-bancario-python?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/tertudev/otimizando-sistema-bancario-python?style=for-the-badge)

## 🧐 Sobre o Projeto

Este repositório apresenta uma implementação simplificada de um sistema bancário, desenvolvido em Python. O principal objetivo é servir como uma ferramenta didática para a prática e consolidação de conceitos fundamentais da programação, como variáveis, estruturas condicionais (`if`, `elif`, `else`), laços de repetição (`while`), manipulação de entrada e saída de dados (`input()`, `print()`) e formatação de strings.

A abordagem técnica foca na clareza e na aplicação direta desses conceitos, resultando em um script procedural que gerencia o estado da conta (saldo, extrato, número de saques diários) em memória. Não são utilizados padrões de projeto complexos ou bibliotecas externas, mantendo o foco na lógica de negócio e na sintaxe básica do Python. O projeto é ideal para iniciantes que desejam entender como construir uma aplicação interativa do zero, aplicando a lógica de programação em um cenário prático.

## ✨ Funcionalidades

O sistema oferece as seguintes operações básicas, acessíveis através de um menu interativo:

*   **Depositar:** Permite ao usuário adicionar fundos à sua conta. O sistema valida que apenas valores positivos sejam aceitos para depósito.
*   **Sacar:** Habilita a retirada de dinheiro da conta, aplicando um conjunto de regras de negócio:
    *   Limite máximo de R$ 500,00 por saque.
    *   Limite diário de 3 transações de saque.
    *   Verificação de saldo disponível para garantir que a conta não fique negativa.
*   **Extrato:** Exibe um histórico detalhado de todas as movimentações realizadas (depósitos e saques), incluindo os valores e o tipo de operação.
*   **Sair:** Encerra a execução do programa de forma segura.

## 🛠️ Tecnologias

Este projeto foi desenvolvido utilizando as seguintes tecnologias e conceitos:

*   **Linguagem:** Python 3.x
*   **Conceitos Aplicados:**
    *   Variáveis para armazenamento de estado (saldo, extrato, contador de saques).
    *   Operadores aritméticos para cálculos de saldo.
    *   Estruturas de decisão (`if`, `elif`, `else`) para validação de regras de negócio e controle de fluxo.
    *   Laços de repetição (`while`) para manter o menu do sistema ativo.
    *   Funções de entrada e saída (`input()`, `print()`) para interação com o usuário.
    *   Manipulação e formatação de `strings` para apresentação do extrato e mensagens.

## 🚀 Como Começar

Para executar este projeto em seu ambiente local, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Você pode baixá-lo do [site oficial do Python](https://www.python.org/downloads/).

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/tertudev/otimizando-sistema-bancario-python.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd otimizando-sistema-bancario-python
    ```

### Execução

1.  **Execute o script principal:**
    ```bash
    python labproject.py
    ```

2.  Siga as instruções apresentadas no terminal para interagir com o sistema bancário.

## 📂 Estrutura

A estrutura do repositório é simples e direta, refletindo a natureza do projeto:

*   `labproject.py`: Contém toda a lógica do sistema bancário, incluindo o menu de opções, as funções de depósito, saque e extrato, e as validações de regras de negócio.
*   `LICENSE`: Arquivo que especifica a licença de uso do projeto.
*   `README.md`: Este arquivo de documentação.
*   `.gitignore`: Define os arquivos e diretórios que devem ser ignorados pelo sistema de controle de versão Git.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum problema, sinta-se à vontade para abrir uma [issue](https://github.com/tertudev/otimizando-sistema-bancario-python/issues) ou enviar um [pull request](https://github.com/tertudev/otimizando-sistema-bancario-python/pulls).

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

Vamos codar o futuro! 🚀
