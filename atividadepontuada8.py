def obter_preco(cor):
    
    tabela_precos = {
        "vermelho": 15.00,
        "azul": 20.00,
        "verde": 25.00,
        "amarelo": 30.00
    }
    
    
    if cor in tabela_precos:
        return tabela_precos[cor]
    else:
        return None  


cor_cd = input("Digite a cor do CD (Vermelho, Azul, Verde, Amarelo): ").strip().lower()


preco = obter_preco(cor_cd)


if preco is not None:
    print(f"O preço do CD {cor_cd.capitalize()} é: R${preco:.2f}")
else:
    print("Cor inválida! As cores disponíveis são: Vermelho, Azul, Verde e Amarelo.")