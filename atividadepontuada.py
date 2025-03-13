
def pode_conceder_emprestimo(renda, valor_emprestimo, num_prestacoes):
  
    valor_maximo_emprestimo = renda * 10
    
    
    valor_maximo_prestacao = renda * 0.30
    
    
    valor_prestacao = valor_emprestimo / num_prestacoes
    
   
    if valor_emprestimo <= valor_maximo_emprestimo and valor_prestacao <= valor_maximo_prestacao:
        return True
    else:
        return False


renda_mensal = float(input("Digite a sua renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor do empréstimo solicitado: R$ "))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))


if pode_conceder_emprestimo(renda_mensal, valor_emprestimo, num_prestacoes):
    print("Empréstimo pode ser concedido!")
else:
    print("Empréstimo NÃO pode ser concedido!")