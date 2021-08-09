class Esconderijo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def obter_dist(self, y):
        """
        Retorna a distância ao quadrado do esconderijo a determinada coordenada y
        """
        return (self.x ** 2 + (self.y - y) ** 2)  # ** 0.5


def obter_maior_dist(y):
    """
    Para determinada coordenada y, retorna a maior distância a um esconderijo
    """
    maior_dist = 0
    for esc in esconderijos:
        if esc.obter_dist(y) > maior_dist:
            maior_dist = esc.obter_dist(y)
    return maior_dist


while True:
    n_esconderijos, muralha_y = [int(x) for x in input().split()]
    if n_esconderijos == 0:
        break

    # Cria uma lista de esconderijos
    esconderijos = []
    for n in range(n_esconderijos):
        pos = input().split()
        esconderijos.append(Esconderijo(int(pos[0]), int(pos[1])))

    # Busca binária
    # Conjunto de procura de 0 até muralha_y
    y_max = muralha_y - 1
    y_min = 0
    while True:
        m = (y_max + y_min) // 2  # Começa analisando ponto médio do conjunto

        # A partir do ponto médio, verifica em que direção a maior distância diminui
        maior_dist_cima = obter_maior_dist(m + 1)
        maior_dist_m = obter_maior_dist(m)
        maior_dist_baixo = obter_maior_dist(m - 1)

        if maior_dist_cima < maior_dist_m:  # maior distância diminui para cima
            y_min = m + 1  # Corta de conjunto procura pela metade
        elif maior_dist_baixo < maior_dist_m:  # maior distância diminui para baixo
            y_max = m - 1  # Corta de conjunto procura pela metade
        else:  # Ponto m tem a maior distância mínima
            print(m)
            break
