#def define uma função 

var = 7 

def mudar_e_imprmir():
    global var
    var = 13
    print ("Variável dentro da função", var)

print ("Variável antes de mudar", var)
mudar_e_imprmir()
print ("Variável depois de mudar", var)