import os
os.system("clear")

lista_numeros = []

QUANTIDADES_NUMEROS = 5

print("= Solicitando numeros =")
for i in range(QUANTIDADES_NUMEROS):
    numero = int(input(f"Digite o {i+1}º numero0: "))
    lista_numeros.append(numero)


maior = max(lista_numeros)
menor = min(lista_numeros)

for i, numero in enumerate(lista_numeros, start=1):
    print(f"{i}º numero: {numero}")


print(f"\nMaior numero: {maior}")
print(f"Menor numero: {menor}")
