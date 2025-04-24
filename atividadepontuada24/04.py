import os 
os.system("clear")

def calcular_inss(salario_base):
    if salario_base <= 1320.00:
        inss = salario_base * 0.075
    elif salario_base <= 2571.29:
        inss = salario_base * 0.09
    elif salario_base <= 3856.94:
        inss = salario_base * 0.12
    elif salario_base <= 7507.49:
        inss = salario_base * 0.14
    else:
        inss = 1051.05  # Teto do INSS
    return inss

def calcular_irrf(salario_base, dependentes):
    if salario_base <= 2112.00:
        irrf = 0.00
    elif salario_base <= 2826.65:
        irrf = salario_base * 0.075 - dependentes * 189.59
    elif salario_base <= 3544.00:
        irrf = salario_base * 0.15 - dependentes * 189.59
    elif salario_base <= 4256.00:
        irrf = salario_base * 0.225 - dependentes * 189.59
    else:
        irrf = salario_base * 0.275 - dependentes * 189.59
    if irrf < 0:
        irrf = 0
    return irrf

def calcular_vale_transporte(salario_base, deseja_vale_transporte):
    if deseja_vale_transporte == 's':
        return salario_base * 0.06
    return 0

def calcular_vale_refeicao(valor_refeicao):
    return valor_refeicao * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def calcular_salario_liquido(salario_base, inss, irrf, vale_transporte, vale_refeicao, plano_saude):
    salario_liquido = salario_base - inss - irrf - vale_transporte - vale_refeicao - plano_saude
    return salario_liquido

# Dados de acesso (independente do valor digitado, sempre será concedido)
matricula = input("Digite a matrícula do funcionário: ")
senha = input("Digite a senha do funcionário: ")

print(f"Acesso concedido para matrícula {matricula}.")

# Dados para cálculos
salario_base = float(input("Digite o salário base do funcionário (R$): "))
dependentes = int(input("Quantos dependentes o funcionário possui? "))
deseja_vale_transporte = input("Deseja receber vale transporte? (s/n): ").strip().lower()
valor_vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))

# Calculando os descontos e acréscimos
inss = calcular_inss(salario_base)
irrf = calcular_irrf(salario_base, dependentes)
vale_transporte = calcular_vale_transporte(salario_base, deseja_vale_transporte)
vale_refeicao = calcular_vale_refeicao(valor_vale_refeicao)
plano_saude = calcular_plano_saude(dependentes)

# Calculando o salário líquido
salario_liquido = calcular_salario_liquido(salario_base, inss, irrf, vale_transporte, vale_refeicao, plano_saude)

# Calculando o total de descontos
total_descontos = inss + irrf + vale_transporte + vale_refeicao + plano_saude

# Exibindo o resultado
print("\nResumo de Descontos e Acréscimos:")
print(f"Salário Base: R${salario_base:.2f}")
print(f"Desconto INSS: R${inss:.2f}")
print(f"Desconto IRRF: R${irrf:.2f}")
print(f"Desconto Vale Transporte: R${vale_transporte:.2f}")
print(f"Desconto Vale Refeição: R${vale_refeicao:.2f}")
print(f"Desconto Plano de Saúde: R${plano_saude:.2f}")
print(f"Total de Descontos: R${total_descontos:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")