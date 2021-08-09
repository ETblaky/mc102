import sys

def log_2(x):
    """
    Calcula o log de x na base 2
    """
    if 2 > x:
        return 0
    return log_2(x / 2) + 1


def piso(x):
    """
    Arrendonda x para o menor inteiro mais proximo
    """
    return int(x // 1)


def encaixar_quadrado(i):
    """
    Tenta encaixar um quadrado de lado 2^i no retangulo m,n
    """
    if i >= 0:  # se i < 0, termina a recursão
        linhas_possiveis = []  # precisa achar 2^i linhas com pelo menos 2^i quadrados disponíveis
        for j in range(min(m, n)):
            if len(linhas_possiveis) == 2 ** i:
                break  # não queremos ocupar mais que 2^i linhas
            if espaco_livre[j] >= 2 ** i:
                linhas_possiveis.append(j)
            else:
                linhas_possiveis.clear()
        if len(linhas_possiveis) >= 2 ** i:  # caso o quadrado caiba no mapa
            for linha in linhas_possiveis:
                espaco_livre[linha] -= 2 ** i  # retira das linhas o espaço ocupado
            if i in submagias:  # e declara que foi utilizado (mais) 1 submagia de nivel i
                submagias[i] += 1
            else:
                submagias[i] = 1
            encaixar_quadrado(i)  # se o quadrado coube, testa se outro de mesma dimensão caberia
        else:
            encaixar_quadrado(i - 1)  # se não coube, testa um quadrado menor


sys.setrecursionlimit(2500)

m, n = [int(x) for x in input().split()]
espaco_livre = [max(m, n) for j in range(min(m, n))]  # Cria uma lista com o espaço livre em cada linha do mapa
submagias = dict()  # A lista contem o menor número de elementos por otimização
submagias_total = 0
PM_gasto = 0

encaixar_quadrado(piso(log_2(min(m, n))))

print("---")
print("Grimorio de Teraf L'are")
print("---")
for nivel in sorted(list(submagias.keys())):
    submagias_total += submagias[nivel]
    PM_gasto += submagias[nivel] * (2 ** nivel)
    print(submagias[nivel], "submagia(s) de nivel", nivel)
print("---")
print("Total de submagia(s) conjurada(s):", submagias_total)
print("Total de PM gasto:", PM_gasto)
print("---")
