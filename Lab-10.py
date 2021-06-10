dossies = {}
evidencias = {}

linha = ""
while linha != "--":
    nome = input().split(": ")[1]
    dossies[nome] = {}
    linha = input()
    while "-" not in linha:
        chave, valor = linha.split(": ")
        dossies[nome][chave] = valor
        linha = input()

linha = input()
while linha != "---":
    chave, valor = linha.split(": ")
    evidencias[chave] = valor
    linha = input()

suspeitos = []

for dossie in dossies.keys():
    contem_evidencias = []
    for evidencia in evidencias.keys():
        contem_evidencias.append(evidencia in dossies[dossie].keys() and dossies[dossie][evidencia] == evidencias[evidencia])
    if False not in contem_evidencias:
        suspeitos.append(dossie)

if len(suspeitos) > 0:
    print("Suspeito" + ("(a):" if len(suspeitos) == 1 else "s(as):"))
else:
    print("Nenhum suspeito(a) com essas caracteristicas foi identificado(a).")

for suspeito in sorted(suspeitos):
    print(suspeito)
