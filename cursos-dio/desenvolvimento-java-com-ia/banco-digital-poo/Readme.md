# Banco Digital

Este é um projeto de um banco digital desenvolvido em Java como parte de uma atividade da [DIO.me](https://www.dio.me/). O objetivo deste projeto é reforçar o conhecimento em Programação Orientada a Objetos (POO) em Java.

## Estrutura do Projeto

O projeto consiste nas seguintes classes e interfaces:

- `Banco`: Gerencia os clientes e contas do banco.
- `Cliente`: Representa os clientes do banco.
- `Conta` (abstract): Classe base para as contas, implementando a interface `IConta`.
- `ContaCorrente`: Extensão da classe `Conta` representando uma conta corrente.
- `ContaPoupanca`: Extensão da classe `Conta` representando uma conta poupança.
- `IConta` (interface): Define operações bancárias básicas.
- `Main`: Classe principal para demonstrar o uso das classes e funcionalidades.

## Funcionalidades

- Criar contas correntes e poupança.
- Depositar, sacar e transferir dinheiro entre contas.
- Aplicar juros em contas poupança.
- Imprimir extratos de contas.
- Listar todas as contas do banco.

## Tecnologias Utilizadas

- Java
- Lombok (para reduzir a verbosidade do código)

## Como Executar

1. Clone o repositório:
    ```bash
    git clone <URL do repositório>
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd <diretório do projeto>
    ```

3. Compile e execute o projeto:
    ```bash
    javac Main.java
    java Main
    ```

## Exemplo de Uso

Ao executar o projeto, serão demonstradas operações de depósito, saque, transferência e aplicação de juros, além da impressão dos extratos das contas criadas.

## Contribuição

Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests com melhorias ou novas funcionalidades.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

---

Atividade desenvolvida como parte do curso da [DIO.me](https://www.dio.me/).
