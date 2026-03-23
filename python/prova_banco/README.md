# 🏦 Sistema Bancário em Python

Este é um sistema bancário simples feito em Python, que simula as principais operações de uma conta corrente, como depósito, saque, criação de contas e gerenciamento de clientes. O projeto foi desenvolvido com base em um desafio de lógica de programação.

## ✅ Funcionalidades

### 🔹 Desafio 1: Operações Bancárias
- **Depositar:** Aceita apenas valores positivos.
- **Sacar:** 
  - Valor positivo e saldo suficiente.
  - Limite de R$ 500,00 por operação.
  - Limite de 3 saques por dia por conta.
- **Visualizar Extrato:** Mostra o histórico de movimentações no formato `R$ XXXX.XX`.

### 🔹 Desafio 2: Gerenciamento de Clientes e Contas
- **Criar Cliente:** Nome, data de nascimento e CPF (sem pontuação).
- **Criar Conta Corrente:**
  - Número da agência fixo: `0001`.
  - Número da conta é sequencial (1, 2, 3...).
  - Um cliente pode ter múltiplas contas.
  - Cada conta está associada a um cliente válido.
