import os
os.system("clear")

lista_pratos = []

opcao = int(input("""Codigo \t Prato \t\t Valor 
1 \t picanha \t\t R$ 25,00
2 \t lasanha \t\t R$ 20,00
3 \t Pão com ovo \t\t R$ 5,00

Digite a opção desejada:                  
                """))

match opcao:
    case 1:
        prato