import random

def rolar_dados(numero_de_dados):
    i = 1
    lista = []
    while i <= numero_de_dados:
        rolagem = random.randint(1,6)
        lista.append(rolagem)
        i +=1

    return lista
