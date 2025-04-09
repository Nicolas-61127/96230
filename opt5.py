import os 
os.system("clear")


def verificar_impar_par(numero):
    if numero  % 2 == 0:
        print(f"Este numero {numero} e par!")
    else:
        print(f"Este numero {numero} e impar!")


numero_usuario = int(input("Digite um numero :"))
verificar_impar_par(numero_usuario)