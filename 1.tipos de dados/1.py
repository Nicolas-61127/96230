import os 
os.system("clear")
nota1 = int(input("escreva o valor1 :"))
nota2 = int(input("escreva o valor2 :"))
nota3 = int(input("escreva o valor3 :"))
media = (nota1 + nota2 + nota3) /3
print(f"a media sera {media:.2f}")
if media >= 7.0:
    print("Aluno em aprovado")
elif media <= 4.00:
    print("Aluno recuperaçao")
else:
    print("Aluno reprovado")      