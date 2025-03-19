import os
os.system("clear")

idade = int(input("digite a sua idade :"))

while idade < 18:
    print("somente maiores de 18 anos.\n")
    idade = int(input("digite a sua idade :"))

print("FIM")