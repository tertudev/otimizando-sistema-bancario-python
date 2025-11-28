# 🏦 Sistema Bancário em Python

Este é um **sistema bancário simples**, desenvolvido em Python como parte do **Lab Project** do Bootcamp.  
O objetivo é simular operações bancárias básicas, permitindo depósitos, saques, consulta de extrato e encerramento da aplicação, de forma prática e didática.

O projeto é ótimo para quem está começando a aprender Python, praticando lógica, condicionais, loops e manipulação de dados em Python.

## 📌 Funcionalidades

O sistema oferece:

- **Depósito (`d`)**: adicionar valores positivos ao saldo.  
- **Saque (`s`)**:  
  - Limite de **R$ 500,00** por saque.  
  - Máximo de **3 saques diários**.  
  - Verifica saldo suficiente antes da operação.  
- **Extrato (`e`)**: mostra todas as movimentações realizadas e o saldo atual.  
- **Sair (`q`)**: encerra a aplicação.

## ⚙️ Tecnologias utilizadas

- [Python 3](https://www.python.org/) 🐍  
- [Visual Studio Code](https://code.visualstudio.com/) 💻  
- Estrutura de projeto organizada:
## 📦 sistema-bancario
##### ┣ 📜 main.py # Código principal do sistema bancário
##### ┗ 📜 README.md # Documentação do projeto

- Código simples, legível e seguindo boas práticas de Python.

## 🚀 Como executar

Para rodar o sistema, siga os passos abaixo:

```bash
git clone https://github.com/tertudev/otimizando-sistema-bancario-python.git
cd otimizando-sistema-bancario-python
python main.py

# 📊 Exemplo de uso

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 200

=> s
Informe o valor do saque: 50

=> e

================ EXTRATO ================
Depósito: R$ 200.00
Saque: R$ 50.00

Saldo: R$ 150.00
=========================================
