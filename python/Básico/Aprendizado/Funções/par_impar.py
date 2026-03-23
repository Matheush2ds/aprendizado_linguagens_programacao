num = int(input("Digite um número: "))

def par_impar(num):
    if num % 2 == 0:
        return f'O número {num} é par!'
    else:
        return f'O número {num} é impar!'

resultado = par_impar(num)
print(resultado)