def desenhar_quadrado(y, x, l, linha=0):
    """
    Para cada ponto da matriz, verifica se ele está dentro do quadrado
    A função desenha uma linha por vez
    """
    if linha == linhas:
        return
    for coluna in range(colunas):
        if abs(coluna - x) <= (l - 1) / 2 and abs(linha - y) <= (l - 1) / 2:
            quadro_final[linha][coluna] = "x"
    # Chama a função de novo para desenhar a próxima linha
    desenhar_quadrado(y, x, l, linha + 1)


def desenhar_circulo(y, x, r, linha=0):
    """
    Para cada ponto da matriz, se d(p, c) <= r, desenha "x"
    A função desenha uma linha por vez
    """
    if linha == linhas:
        return
    for coluna in range(colunas):
        if ((coluna - x) ** 2 + (linha - y) ** 2) ** 0.5 <= r:
            quadro_final[linha][coluna] = "x"
    # Chama a função de novo para desenhar a próxima linha
    desenhar_circulo(y, x, r, linha + 1)


linhas, colunas = [int(x) for x in input().split()]
quantidade_formas = int(input())

# Cria a matriz que contem o desenho
quadro_final = [["-" for i in range(colunas)] for j in range(linhas)]

# Para cada input de figura, desenhe na matriz
for i in range(quantidade_formas):
    forma = input().split()
    tipo = forma[0]
    if tipo == "quadrado":
        desenhar_quadrado(int(forma[1]), int(forma[2]), int(forma[3]))
    else:
        desenhar_circulo(int(forma[1]), int(forma[2]), int(forma[3]))

# Imprima a matriz na formatação certa
for i in range(linhas):
    print(' '.join(quadro_final[i]))
