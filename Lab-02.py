nome_canal = input()
n_contagens = int(input())

views_total = 0
contagem_total = 0

info = {
    "2018": {
        "views": 0,
        "contagens": 0
    },
    "2019": {
        "views": 0,
        "contagens": 0
    },
    "2020": {
        "views": 0,
        "contagens": 0
    }
}

for i in range(n_contagens):
    data = input()
    n_vizualizacao = int(input())

    ano = data.split("-")[0]
    if ano in info.keys():
        views_total += n_vizualizacao
        contagem_total += 1

        info[ano]["views"] += n_vizualizacao
        info[ano]["contagens"] += 1

print("Canal:", nome_canal)
print("Total de views do trienio:", views_total)
print("Media de views do trienio:", "{:.2f}".format(round(views_total / contagem_total, 2)))

for ano in info.keys():
    print()
    print(ano)
    print("Total:", str(info[ano]["views"]))
    print("Porcentagem das views do trienio:", "indeterminada" if views_total == 0 else "{:.2f}".format(round(100 * info[ano]["views"] / views_total, 2)))
    print("Media:", "{:.2f}".format(round(info[ano]["views"] / info[ano]["contagens"], 2)))

