import os
os.system("clear")

def positivo_negativo(numero):
    if numero == 0:
        print("Numero neutro.")
    elif numero >= 1:
        print("numero positivo")
    elif numero < 0:
        print("numero negativo")
print("= POSITIVO OU NEGATIVO =")
numero = int(input("Digite seu numero: "))
positivo_negativo(numero)