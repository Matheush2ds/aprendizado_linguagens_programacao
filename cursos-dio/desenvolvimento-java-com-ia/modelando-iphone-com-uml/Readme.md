# Diagrama UML e Implementação das Funcionalidades

## Objetivo
Este projeto tem como objetivo criar um diagrama UML que represente as funcionalidades de um reprodutor musical, um aparelho telefônico e um navegador na internet. Opcionalmente, as classes e interfaces correspondentes serão implementadas em Java.

Este projeto foi desenvolvido como parte de um exercício para a Digital Innovation One (DIO).

## Funcionalidades a Modelar

### Reprodutor Musical
Um reprodutor musical com os seguintes métodos:
- `tocar()`: Inicia a reprodução da música.
- `pausar()`: Pausa a música em reprodução.
- `selecionarMusica(String musica)`: Seleciona uma música específica para reprodução.

### Aparelho Telefônico
Um aparelho telefônico com os seguintes métodos:
- `ligar(String numero)`: Realiza uma chamada para o número especificado.
- `atender()`: Atende uma chamada recebida.
- `iniciarCorreioVoz()`: Inicia o correio de voz.

### Navegador na Internet
Um navegador na internet com os seguintes métodos:
- `exibirPagina(String url)`: Exibe a página da web no URL especificado.
- `adicionarNovaAba()`: Adiciona uma nova aba no navegador.
- `atualizarPagina()`: Atualiza a página da web atual.

## Diagrama UML
A seguir, encontra-se o diagrama UML que representa as funcionalidades descritas acima:

```mermaid
---
title: Functionalities Diagram
---
classDiagram
    ReprodutorMusical --|> tocar : has
    ReprodutorMusical --|> pausar : has
    ReprodutorMusical --|> selecionarMusica : has
    
    AparelhoTelefonico --|> ligar : has
    AparelhoTelefonico --|> atender : has
    AparelhoTelefonico --|> iniciarCorreioVoz : has
    
    NavegadorInternet --|> exibirPagina : has
    NavegadorInternet --|> adicionarNovaAba : has
    NavegadorInternet --|> atualizarPagina : has
    
    class ReprodutorMusical {
        +tocar()
        +pausar()
        +selecionarMusica(String musica)
    }
    
    class AparelhoTelefonico {
        +ligar(String numero)
        +atender()
        +iniciarCorreioVoz()
    }
    
    class NavegadorInternet {
        +exibirPagina(String url)
        +adicionarNovaAba()
        +atualizarPagina()
    }
