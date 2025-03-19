import os

os.system("cls ||clear")

contador = 0
continua = 'n'

while continua == "s":
    print("repentido......")

    continua = input("tecla 's' se deseja continuar:")
    contador += 1

    if continua != "s":
        break

    if contador == 0:
        print("o bloco nao foi repetido.")

    else:
        print(f"o bloco foi repetido {contador} vezes")