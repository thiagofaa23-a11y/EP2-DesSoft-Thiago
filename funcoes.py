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

def calcula_pontos_soma(dados):
    total = 0
    for dado in dados:
        total += dado

    return total

def calcula_pontos_sequencia_baixa(dados):
    presenca = [0] * 7
    

    for valor in dados:
        presenca[valor] = 1
        
    sequencia = 0

    for i in range(1, 7):

        if presenca[i] == 1:
            sequencia += 1

            if sequencia == 4:
                return 15
            
        else:
            sequencia = 0 
            
    return 0

def calcula_pontos_sequencia_alta(dados):
    presenca = [0] * 7
    

    for dado in dados:
        presenca[dado] = 1
        
    sequencia = 0

    for i in range(1, 7):

        if presenca[i] == 1:
            sequencia += 1

            if sequencia == 5:
                return 30
            
        else:
            sequencia = 0 
            
    return 0

def calcula_pontos_full_house(dados):

    contagem = [0]*len(dados)
    soma = 0
    i = 0

    for dado in dados:
        contagem[i] = dados.count(dado)
        i+=1

    if 3 in contagem and 2 in contagem:
        for dado in dados:
            soma += dado

    return soma

def calcula_pontos_quadra(dados):

    contagem = 0
    soma = 0
    i = 0

    for dado in dados:

        contagem = dados.count(dado)
        if contagem >= 4:
            for dado in dados:
                soma += dado
            break


    return soma

def calcula_pontos_quina(dados):

    contagem = 0
    soma = 0
    i = 0

    for dado in dados:

        contagem = dados.count(dado)
        if contagem >= 5:
            for dado in dados:
                soma = 50
            break


    return soma
    
def calcula_pontos_regra_avancada(dados):
    resultado = {
        'cinco_iguais': calcula_pontos_quina(dados),

        'full_house': calcula_pontos_full_house(dados),

        'quadra': calcula_pontos_quadra(dados),

        'sem_combinacao': calcula_pontos_soma(dados),

        'sequencia_alta':calcula_pontos_sequencia_alta(dados),

        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados),
    }

    return resultado