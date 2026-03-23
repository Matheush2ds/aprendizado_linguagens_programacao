var = 7

def mudar_e_imprmir(novo_valor_1, novo_valor_2):
    global var
    var = novo_valor_1
    print ("Variável dentro da função após 1º Alteração", var)
    var + novo_valor_2
    print ("Variável dentro da função após 2º Alteração", var)

print ("Variável antes de mudar", var)
mudar_e_imprmir(novo_valor_2=5, novo_valor_1=13)
print ("Variável depois de mudar", var)