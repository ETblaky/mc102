def verificar_senha(s):
    """
    Verifica se s é a senha correta
    :param s: Senha a ser testada
    :return: True se s for a senha correta
    """
    return s == senha


def contar_semelhanca(s):
    """
    Conta quantos digitos são semelhantes entre s e a senha correta
    :param s: Senha a ser comparada com a senha correta
    :return: Quantos digitos são iguais entre s e a senha correta
    """

    semelhanca = 0

    if len(s) != len(senha):
        return "Erro: quantidade de digitos incongruente"

    for j in range(len(senha)):
        if list(s)[j] == list(senha)[j]:
            semelhanca += 1

    return semelhanca


info = input().split(' ')
senha = info[0]
tentativas = int(info[1])

for i in range(tentativas):
    senha_testada = input()

    if verificar_senha(senha_testada):
        print('Senha reconhecida. Desativando defesas...')
        break
    else:
        tentativas -= 1

        print("Senha incorreta")
        print('Semelhanca:', contar_semelhanca(senha_testada))
        print('Tentativas restantes:', tentativas, '\n')

        if tentativas == 0:
            print('Tentativas esgotadas. Acionando defesas...')
            break
