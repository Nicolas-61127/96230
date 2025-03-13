def calcular_valor(litros, tipo_combustivel):
    
    preco_alcool = 3.00
    preco_gasolina = 4.50

    
    if tipo_combustivel == 'A':
        valor_total = litros * preco_alcool
        desconto = 0.05  
    elif tipo_combustivel == 'G':
        valor_total = litros * preco_gasolina
        desconto = 0.03 
    else:
        return None  

  
    valor_com_desconto = valor_total * (1 - desconto)
    return valor_com_desconto


litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A - Álcool / G - Gasolina): ").strip().upper()


valor_a_pagar = calcular_valor(litros_vendidos, tipo_combustivel)

if valor_a_pagar is not None:
    print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")
else:
    print("Tipo de combustível inválido! Digite 'A' para Álcool ou 'G' para Gasolina.")