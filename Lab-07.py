def codificar(mensagem, enxerto, index):
    """
    Codifica as linhas submetidas usando as regras enunciadas.
    :param mensagem: Linha a ser codificada
    :param enxerto: Enxerto a ser considerado durante a codificação
    :param index: A posição da linha dentro da mensagem
    :return: Linha codificada
    """

    mensagem_codificada = []

    if index % 2 == 0:
        mensagem = list(mensagem[::-1])
        for char in mensagem:
            mensagem_codificada.append(oct(ord(char)).replace("0o", "").zfill(enxerto))
    else:
        for char in list(mensagem):
            mensagem_codificada.append(hex(ord(char)).replace("0x", "").zfill(enxerto).upper())

    return ''.join(mensagem_codificada)


def decodificar(mensagem_codificada, enxerto, index):
    """
    Decodifica as linhas submetidas usando o inverso das regras de codificação
    :param mensagem_codificada: Linha a ser decodificada
    :param enxerto: Enxerto a ser considerado durante a decodificação
    :param index: A posição da linha dentro da mensagem
    :return: Linha decodificada
    """

    mensagem = []
    mensagem_codificada = list(mensagem_codificada)

    if index % 2 == 0:
        for i in range(len(mensagem_codificada) // enxerto):
            char = ''.join(mensagem_codificada[enxerto * i:enxerto * i + enxerto])
            mensagem.append(chr(int(char, 8)))
        mensagem = list(mensagem[::-1])
    else:
        for j in range(len(mensagem_codificada) // enxerto):
            char = ''.join(mensagem_codificada[enxerto * j:enxerto * j + enxerto])
            mensagem.append(chr(int(char, 16)))

    return ''.join(mensagem)


info = input().split(" ")
modo = int(info[0])
enxerto = int(info[1])
linhas = int(info[2])

for i in range(linhas):
    linha = input()
    print([codificar, decodificar][modo - 1](linha, enxerto, i + 1))
