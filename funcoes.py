import random

def rolar_dados(numero_de_dados):
    i = 1
    lista = []
    while i <= numero_de_dados:
        rolagem = random.randint(1,6)
        lista.append(rolagem)
        i +=1

    return lista

def guardar_dado(dados_rolados,dados_guardados,dado_selecionado):
    
    dados_guardados.append(dados_rolados[dado_selecionado])
    del dados_rolados[dado_selecionado]
    saida = [dados_rolados, dados_guardados]

    return saida

def remover_dado(dados_rolados,dados_guardados,dado_selecionado):

    dados_rolados.append(dados_guardados[dado_selecionado])
    del dados_guardados[dado_selecionado]
    saida = [dados_rolados, dados_guardados]

    return saida

def calcula_pontos_regra_simples(dados):
    dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for dado in dados:
        dic[dado] += dado
    
    return dic