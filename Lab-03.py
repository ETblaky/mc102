n = int(input())


def print_tabuleiro(n, tabuleiro):
    for i in range(n + 1):
        print(n - i if i != n else " ", end=" ")
        for j in range(n):
            if i == n:
                print(chr(ord("a") + j), end=" ")
            else:
                print(tabuleiro[n - 1 - i][j], end=" " if j != (n - 1) else "\n")
    print("\n")


def verificar_pos(i, j, n):
    return 0 <= j < n and 0 <= i < n


while n != 0:
    info = input().split(" ")
    peca = info[0]
    pos_x = ord(info[1]) - 97
    pos_y = int(info[2]) - 1

    tabuleiro = [["-" for y in range(n)] for x in range(n)]

    if peca == "Torre":
        tabuleiro[pos_y] = ["x" for i in range(n)]
        for j in range(n):
            tabuleiro[j][pos_x] = "x"

    elif peca == "Bispo":
        for i in range(n):
            for j in range(n):
                if abs(i - pos_x) == abs(j - pos_y):
                    tabuleiro[j][i] = "x"

    elif peca == "Dama":
        tabuleiro[pos_y] = ["x" for i in range(n)]
        for i in range(n):
            for j in range(n):
                tabuleiro[j][pos_x] = "x"
                if abs(i - pos_x) == abs(j - pos_y):
                    tabuleiro[j][i] = "x"

    elif peca == "Rei":
        for i in range(pos_x - 1, pos_x + 2):
            for j in range(pos_y - 1, pos_y + 2):
                if verificar_pos(i, j, n):
                    tabuleiro[j][i] = "x"

    elif peca == "Cavalo":
        for i in range(pos_x - 2, pos_x + 3):
            for j in range(pos_y - 2, pos_y + 3):
                if abs(i - pos_x) + abs(j - pos_y) == 3 and verificar_pos(i, j, n):
                    tabuleiro[j][i] = "x"

    elif peca == "Peao":
        if pos_y != n - 1:
            tabuleiro[pos_y + 1][pos_x] = "x"
            if pos_y == 1:
                tabuleiro[pos_y + 2][pos_x] = "x"

    tabuleiro[pos_y][pos_x] = "o"

    print("Movimentos para a peca " + peca + " a partir da casa", info[1] + info[2] + ".")
    print_tabuleiro(n, tabuleiro)

    n = int(input())
