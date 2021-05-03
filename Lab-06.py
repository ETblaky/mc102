class Medalutador:
    def __init__(self, ID, H, K, A_bonus, D_bonus):
        self.ID = ID
        self.H = H
        self.max_H = H
        self.K = K

        # Armazena as pontuações das peças dos respectivos tipos
        self.pecas = {
            "T": [],
            "E": [],
            "D": [],
            "P": [],
        }
        # O número n abaixo representa a posição na lista "pecas" da peça equipada
        self.pecas_equipadas = {
            "T": 0,
            "E": 0,
            "D": 0,
            "P": 0,
        }

        self.ultima_peca_adicionada = []

        self.A_bonus = A_bonus
        self.D_bonus = D_bonus

        self.A = 0
        self.D = 0

    def obter_ID(self):
        return self.ID

    def obter_H(self):
        return self.H

    def definir_H(self, H):
        self.H = H

    def repor_H(self):
        self.H = min(self.K + self.H, self.max_H)

    def obter_A(self):
        return self.A

    def obter_D(self):
        return self.D

    def adicionar_peca(self, tipo, pontos):
        self.pecas[tipo].append(pontos)
        self.ultima_peca_adicionada = [tipo, pontos]
        return len(self.pecas[tipo]) - 1

    def obter_ultima_peca_adicionada(self):
        return self.ultima_peca_adicionada

    def obter_peca(self, tipo, index):
        return self.pecas[tipo][index]

    # Escolhe melhor peça para equipar de cada tipo
    def calcular_peca_equipada(self):
        for peca in ["T", "E", "D", "P"]:
            for i in range(len(self.pecas[peca])):
                if self.pecas[peca][i] > self.obter_peca_equipada(peca):
                    self.definir_peca_equipada(peca, i)
        self.recalcular_AD()

    # Retorna a pontuação da peça equipada do determinado tipo
    def obter_peca_equipada(self, tipo):
        if self.pecas_equipadas[tipo] == -1:  # Se não tiver uma peça equipada
            return 0  # Então retorne uma pontuação zero.
        return self.pecas[tipo][self.pecas_equipadas[tipo]]

    def definir_peca_equipada(self, tipo, index):
        self.pecas_equipadas[tipo] = index

    def remover_peca_equipada(self, tipo):
        self.pecas[tipo].pop(self.pecas_equipadas[tipo])
        self.pecas_equipadas[tipo] = -1  # Ou seja, não tem peça equipada

    def recalcular_AD(self):
        self.A = self.obter_peca_equipada("E") + self.obter_peca_equipada("D") + self.A_bonus
        self.D = self.obter_peca_equipada("T") + self.obter_peca_equipada("P") + self.D_bonus

    def ficha_tecnica(self):
        return \
            f'\tA{self.ID} = E{self.pecas["E"][self.pecas_equipadas["E"]]} + D{self.pecas["D"][self.pecas_equipadas["D"]]} + {self.A_bonus} = {self.A}\n' \
            f'\tD{self.ID} = T{self.pecas["T"][self.pecas_equipadas["T"]]} + P{self.pecas["P"][self.pecas_equipadas["P"]]} + {self.D_bonus} = {self.D}\n' \
            f'\tH{self.ID} = {self.H}'

    def __repr__(self):
        return str(self.ID)


def batalhar(i, j):
    if (i.obter_A() > j.obter_D() or j.obter_A() > i.obter_D()) and i.obter_A() - j.obter_D() != j.obter_A() - i.obter_D():
        vencedor = i if i.obter_A() - j.obter_D() > j.obter_A() - i.obter_D() else j
    elif i.obter_H() != j.obter_H():
        vencedor = i if i.obter_H() > j.obter_H() else j
    else:
        vencedor = i if i.obter_ID() < j.obter_ID() else j

    perdedor = j if id(vencedor) == id(i) else i

    # Recalcular habilidade de cada um
    vencedor.definir_H(max(vencedor.obter_H() - perdedor.obter_H(), 0))
    perdedor.definir_H(perdedor.obter_H() // 2)

    # Achar melhor peça para dar para o vencedor
    peca_trocada = "T"
    dif_pontos = perdedor.obter_peca_equipada("T") - vencedor.obter_peca_equipada("T")
    for peca in ["E", "D", "P"]:
        if perdedor.obter_peca_equipada(peca) - vencedor.obter_peca_equipada(peca) > dif_pontos:
            peca_trocada = peca
            dif_pontos = perdedor.obter_peca_equipada(peca) - vencedor.obter_peca_equipada(peca)

    # Dar peça ao vencedor e remove-la do perdedor
    vencedor.adicionar_peca(peca_trocada, perdedor.obter_peca_equipada(peca_trocada))
    perdedor.remover_peca_equipada(peca_trocada)

    vencedor.calcular_peca_equipada()
    perdedor.calcular_peca_equipada()

    vencedor.repor_H()
    perdedor.repor_H()

    return vencedor


def imprimir_ficha_tecnica(i, j):
    print(i.ficha_tecnica())
    print(j.ficha_tecnica())


def imprimir_resultado_da_batalha(k):
    peca = k.obter_ultima_peca_adicionada()
    print(f'Medalutador {k} venceu e recebeu a {peca[0]}{peca[1]}\n')


def simular_torneios_de_cyberlutas(lista_de_medalutadores):
    lista_torneio_principal = []
    lista_de_repescagem = []

    for medalutador in lista_de_medalutadores:
        lista_torneio_principal.append(medalutador)

    while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
        lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
        lista_de_repescagem = aplicar_rodada_de_batalhas(lista_de_repescagem, None)

    i = lista_torneio_principal.pop(0)
    j = lista_de_repescagem.pop(0)
    print('Cyberluta Final')
    print(f'Medalutadores: {i} vs {j}')
    imprimir_ficha_tecnica(i, j)

    k = batalhar(i, j)
    print(f'Campeao: medalutador {k}')


def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
    if len(lista_de_medalutadores) < 2:
        return lista_de_medalutadores

    lista_de_vencedores = []
    while len(lista_de_medalutadores) >= 2:
        i = lista_de_medalutadores.pop(0)
        j = lista_de_medalutadores.pop(0)

        if i.obter_ID() > j.obter_ID():
            i, j = j, i

        if lista_de_repescagem is not None:
            print('Cyberluta do Torneio Principal')
        else:
            print('Cyberluta da Repescagem')

        print(f'Medalutadores: {i} vs {j}')
        imprimir_ficha_tecnica(i, j)

        k = batalhar(i, j)
        imprimir_resultado_da_batalha(k)

        if lista_de_repescagem is not None:
            if i == k:
                lista_de_repescagem.append(j)
            else:
                lista_de_repescagem.append(i)

        lista_de_vencedores.append(k)

    lista_de_vencedores.extend(lista_de_medalutadores)
    return lista_de_vencedores


N = int(input())
lista_de_medalutadores = []
for i in range(N):
    info = input().split(" ")
    H = int(info[0])
    K = int(info[1])
    M = int(info[2])

    info = input().split(" ")
    A_bonus = int(info[0])
    D_bonus = int(info[1])

    medalutador = Medalutador(i + 1, H, K, A_bonus, D_bonus)

    for j in range(M):
        peca = input().split(" ")
        tipo = peca[0]
        pontos = int(peca[1])

        index_peca = medalutador.adicionar_peca(tipo, pontos)
        if pontos > medalutador.obter_peca_equipada(tipo):
            medalutador.definir_peca_equipada(tipo, index_peca)

    medalutador.recalcular_AD()
    lista_de_medalutadores.append(medalutador)

simular_torneios_de_cyberlutas(lista_de_medalutadores)
