frutas = int(input("""
1. MAÇÃ
2. MORANGO

Digite uma opção: 
"""))

match frutas:
    case 1:  
        quantidade_fruta = int(input("Digite a quantidade de maçãs (em Kg): "))
        if quantidade_fruta <= 5:
            valor_compra = quantidade_fruta * 1.80  
            print(f"Valor da compra: R${valor_compra:.2f}")  
        else:
            valor_compra = quantidade_fruta * 1.80 
            if valor_compra > 15.00:  
                desconto = valor_compra * 0.10 
                valor_final = valor_compra - desconto
                print(f"Valor da compra com desconto: R${valor_final:.2f}")
            else:
                print(f"Valor da compra: R${valor_compra:.2f}")
                
    case 2:  
        quantidade_fruta = int(input("Digite a quantidade de morangos (em Kg): "))
        if quantidade_fruta <= 5:
            valor_compra = quantidade_fruta * 2.50  
            print(f"Valor da compra: R${valor_compra:.2f}")
        else:
            valor_compra = quantidade_fruta * 2.50 
            if valor_compra > 15.00:  
                desconto = valor_compra * 0.10  
                valor_final = valor_compra - desconto
                print(f"Valor da compra com desconto: R${valor_final:.2f}")
            else:
                print(f"Valor da compra: R${valor_compra:.2f}")
    
