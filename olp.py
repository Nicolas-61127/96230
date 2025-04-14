import os
os.system("clear")

lista_notas = []
QUANTIDADES_NOTAS = 4

for i in range(QUANTIDADES_NOTAS):
    nota = float(input("Digite sua nota: "))
    lista_notas.append(nota)


media = sum(lista_notas) / QUANTIDADES_NOTAS

print()
for nota in lista_notas:
    print(nota)

print(f"Media: {media}")
 
if media < 7:
    print("aluno reprovado")
else:
    print("aluno aprovado")