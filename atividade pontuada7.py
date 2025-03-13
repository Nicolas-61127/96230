nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário do produto: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02  
elif quantidade <= 10:
    desconto = total * 0.03  
else:
    desconto = total * 0.05  

total_a_pagar = total - desconto

print(f"\nResumo da compra:")
print(f"Produto: {nome_produto}")
print(f"Quantidade adquirida: {quantidade}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Total: R${total:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${total_a_pagar:.2f}")