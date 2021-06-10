dimensao = [int(x) for x in input().split()]

while dimensao[0] != 0 and dimensao[1] != 0:
    matriz_M = []
    matriz_N = []

    todos_elementos = []

    for i in range(dimensao[0]):
        matriz_M.extend([[]])
        for j in input().split():
            matriz_M[i].extend([int(j)])
            todos_elementos.extend([int(j)])

    for i in range(dimensao[1]):
        matriz_N.extend([[]])
        for j in input().split():
            matriz_N[i].extend([int(j)])
            todos_elementos.extend([int(j)])

    elemento_visto = {}  # Quantas vezes o elemento se repetiu (na prática não passa de 2x)
    elementos_comuns = []  # Interseção das matrizes

    for elemento in todos_elementos:
        if elemento not in elemento_visto:
            elemento_visto[elemento] = 1  # Se elemento não estiver no set, então declarar que ele foi visto 1x
        else:
            if elemento_visto[elemento] == 1:  # Se o elemento já foi visto apenas 1x, adiciona-lo a lista da interseção
                elementos_comuns.append(elemento)
            elemento_visto[elemento] += 1  # Declara que elemento foi visto +1x,senão "elementos_comuns" teria repetidos


    matriz_menor = matriz_M if dimensao[0] < dimensao[1] else matriz_N

    # Remove da matriz menor os elementos em comum e M e N
    for elemento in elementos_comuns:
        for i in range(len(matriz_menor)):
            if elemento in matriz_menor[i]:
                matriz_menor[i].remove(elemento)

    resultado = (
        # linhas da matriz maior somado com o número de linhas da matriz menor que não intersecta com a outra
        # len(linha) == min(dimensao) serve para checar se essa linha das matriz menor intersectou com a matriz maior
        max(dimensao) + len(list(filter(lambda linha: len(linha) == min(dimensao), matriz_menor))),
        # colunas da matriz maior somado com o número de colunas da matriz menor que não intersecta com a outra
        # primeiro se gera uma lista com o tamanho de cada linha, então se escolhe o menor valor, pois coincide com o
        # número de colunas que não intersecta
        max(dimensao) + min([len(i) for i in matriz_menor])
    )

    print(resultado[0], "x", resultado[1])

    dimensao = [int(x) for x in input().split()]
