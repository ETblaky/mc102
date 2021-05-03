nome = input()
p_fusao = float(input())  # Celsius
p_ebulicao = float(input())  # Celsius
temp_atual_f = float(input())  # Fahrenheit

temp_atual_c = round((temp_atual_f - 32) * 5 / 9, 2)
estado_fisico = ""

if temp_atual_c >= p_ebulicao:
    estado_fisico = "Gasoso"
elif temp_atual_c >= p_fusao:
    estado_fisico = "Liquido"
else:
    estado_fisico = "Solido"

print("Material:", nome)
print("Ponto de fusao (Celsius):", format(p_fusao, ".2f"))
print("Ponto de ebulicao (Celsius):", format(p_ebulicao, ".2f"))
print("Temperatura atual (Celsius):", format(temp_atual_c, ".2f"))
print("Estado fisico do material:", estado_fisico)
