def ord_segunda(endereco):
    chars_minusculos = 0
    for caractere in list(endereco):
        chars_minusculos += 1 if caractere.islower() else 0
    return chars_minusculos


def ord_terca(endereco):
    chars_maiusculos = 0
    for caractere in list(endereco):
        chars_maiusculos += 1 if caractere.isupper() else 0
    return chars_maiusculos


def ord_quarta(endereco):
    letras = 0
    for caractere in list(endereco):
        letras += 1 if ord('A') <= ord(caractere) <= ord('z') else 0
    return letras


def ord_quinta(endereco):
    return len(endereco.split(" "))


def ord_sexta(endereco):
    soma = 0
    for caractere in list(endereco):
        soma += ord(caractere)
    return soma


ordenar = {
    "Segunda": {"key": ord_segunda, "reverse": False},
    "Terca": {"key": ord_terca, "reverse": True},
    "Quarta": {"key": ord_quarta, "reverse": False},
    "Quinta": {"key": ord_quinta, "reverse": False},
    "Sexta": {"key": ord_sexta, "reverse": True}
}

info = input().split(" ")
dia = info[0]
n_enderecos = int(info[1])

enderecos = []

for i in range(n_enderecos):
    enderecos.append(input())

enderecos = sorted(enderecos, **ordenar[dia])

for i in range(n_enderecos):
    print(enderecos[i])
