import os 
os.system("clear")
def inflacionar(preco):
    if preco < 100:
        resultado = preco * 1.10
    else:
        resultado * 1.20
    return resultado

preco_produto = float(input("Digite o preco do produto :"))

preco_inflacionado = inflacionar(preco_produto)

print(f"preco final: {preco_inflacionado}")