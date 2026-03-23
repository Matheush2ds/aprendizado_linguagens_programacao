def soma_numero(calculo):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    match calculo:
        case 1:
            resultado = num1 + num2
            print ("A soma entre", num1, "e", num2, "Resulta em: ", resultado)
        case 2:
            resultado = num1 - num2
            print ("A subtração entre", num1, "e", num2, "Resulta em: ", resultado)
        case 3:
            resultado = num1 / num2
            print ("A divisão entre", num1, "e", num2, "Resulta em: ", resultado)
        case 4:
            resultado = num1 * num2
            print ("A multiplicação entre", num1, "e", num2, "Resulta em: ", resultado)

print("O que gostaria de fazer? \n1-Somar \n2-Subtrair \n3-Dividir \n4-Multiplicar")
opcao = int(input("Escolha uma opção (1 a 4): "))
soma_numero(opcao)
