import os
os.system("clear")

def exibir_tabuada(numero):
    print(f"Tabuada do {numero}")
    for i in range (1,11):
        print(f"{numero} x {i} = {numero * i}")

        numero_usuario = int(input("informe o numero"))
        exibir_tabuada(numero_usuario)