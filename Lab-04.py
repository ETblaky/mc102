info = input().split(' ')
senha = info[0]
tentativas = int(info[1])


def verificar_senha(s):
    return s == senha


def contar_semelhanca(s):
    semelhanca = 0
    if len(s) != len(senha):
        return "Erro: quantidade de digitos incongruente"
    for j in range(len(senha)):
        if list(s)[j] == list(senha)[j]:
            semelhanca += 1
    return semelhanca


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
