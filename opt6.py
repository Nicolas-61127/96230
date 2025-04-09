import os
os.system("clear")

def positivo_negativo(numero):
    if numero < 0:
        print("Numero negativo.")
    else:
        print("numero positivo")

print("= POSITIVO OU NEGATIVO =")
numero = int(input("Digite seu numero: "))
positivo_negativo(numero)