import os 
os.system("clear")
def descontar(preco):
    if preco < 100:
        resultado = preco * 0.9
    else:
        resultado = preco * 0.8
        
    return resultado

preco_produto = float(input("Digite o preco do produto :"))

preco_descontado = descontar(preco_produto)

print(f"preco final: {preco_descontado}")