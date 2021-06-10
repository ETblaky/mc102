def resolver(linha):
    """
    Decide se entre resolver um expressao aritimetica, booleana simples e booleana composta dependendo da linha entrada.
    :param linha: Linha a ser processada
    :return: o resultado da expressão se for o caso.
    """
    elementos = linha.split(" ")

    if "=" in linha and elementos[1] == "=":
        atribuicao(linha)

    else:
        if any(operador in linha for operador in ["OR", "AND"]):
            return resolver_exp_bool_composta(linha)
        elif any(operador in linha for operador in ["==", "!=", "<", "<=", ">", ">="]):
            return resolver_exp_bool_simples(linha)
        else:
            return resolver_exp_aritimetica(linha)


def atribuicao(linha):
    """
    Atribui um valor a uma variavel
    :param linha: linha de atribuicao
    """
    info = [dado.strip() for dado in linha.split("=", 1)]
    if info[0].isnumeric() or info[0][0].isnumeric() or "_" in info[0]:
        print("Erro de sintaxe:", info[0], "nao e um nome permitido para uma variavel.")
    else:
        operandos[info[0]] = resolver(info[1])


def resolver_exp_aritimetica(linha):
    """
    Resolve uma expressao aritimetica
    :param linha: linha com a expressao
    :return: resultado da expressao ou None se ela conter um elemento nao permitido
    """
    elementos = [dado.strip() for dado in linha.split(" ")]
    resultado = 0
    operacao = 0  # 0 -> Soma, 1 -> Subtração

    for elemento in elementos:
        if elemento.isnumeric():
            resultado += int(elemento) if operacao == 0 else -int(elemento)
        elif elemento in ["+", "-"]:
            operacao = elemento == "-"
        else:
            if elemento in operandos:
                resultado += operandos[elemento] if operacao == 0 else -operandos[elemento]
            else:
                print("Erro de referencia: a variavel", elemento, "nao foi definida.")
                return None

    return resultado


def resolver_exp_bool_simples(linha):
    """
    Resolve uma expressao booleana simples
    :param linha: linha com a expressao
    :return: resultado da expressao ou None se ela conter um elemento nao permitido
    """
    res = 0
    if "==" in linha:
        exps = linha.split("==")
        exp_1 = resolver(exps[0].strip())
        exp_2 = resolver(exps[1].strip())
        if exp_1 is None or exp_2 is None:
            return None
        res = exp_1 == exp_2
    elif "!=" in linha:
        exps = linha.split("!=")
        exp_1 = resolver(exps[0].strip())
        exp_2 = resolver(exps[1].strip())
        if exp_1 is None or exp_2 is None:
            return None
        res = exp_1 != exp_2
    elif "<=" in linha:
        exps = linha.split("<=")
        exp_1 = resolver(exps[0].strip())
        exp_2 = resolver(exps[1].strip())
        if exp_1 is None or exp_2 is None:
            return None
        res = exp_1 <= exp_2
    elif "<" in linha:
        exps = linha.split("<")
        exp_1 = resolver(exps[0].strip())
        exp_2 = resolver(exps[1].strip())
        if exp_1 is None or exp_2 is None:
            return None
        res = exp_1 < exp_2
    elif ">=" in linha:
        exps = linha.split(">=")
        exp_1 = resolver(exps[0].strip())
        exp_2 = resolver(exps[1].strip())
        if exp_1 is None or exp_2 is None:
            return None
        res = exp_1 >= exp_2
    else:
        exps = linha.split(">")
        exp_1 = resolver(exps[0].strip())
        exp_2 = resolver(exps[1].strip())
        if exp_1 is None or exp_2 is None:
            return None
        res = exp_1 > exp_2
    return 1 if res else 0


def resolver_exp_bool_composta(linha):
    """
    Resolve uma expressao booleana composta
    :param linha: linha com a expressao
    :return: resultado da expressao ou None se ela conter um elemento nao permitido
    """
    expressoes = [linha]

    for operador in ["AND", "OR"]:
        temp, expressoes = expressoes, []
        for elementos in temp:
            expressoes += [exp.strip() for exp in elementos.split(operador)]

    for i in range(len(expressoes)):
        linha = linha.replace(expressoes[i], "").strip()
        res = resolver(expressoes[i])
        if res is None:
            return None
        expressoes[i] = res

    operadores = linha.split()

    res = expressoes[0]
    for j in range(1, len(expressoes)):
        res = res and expressoes[j] if operadores[j - 1] == "AND" else res or expressoes[j]

    return 1 if res else 0


operandos = {}

while True:
    try:
        linha = input()
        resultado = resolver(linha)
        if resultado is not None:
            print(resultado)

    except EOFError:
        print("Encerrando... Bye-bye.")
        break
