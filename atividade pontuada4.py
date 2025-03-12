a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a == b:
    soma = a + b
    if soma == c:
        print("A soma de a e b é igual a c.")
    else:
        print("A soma de a e b não é igual a c.")
elif a != b:
    soma = a * b
    if soma == c:
        print("O produto de a e b é igual a c.")
    else:
        print("O produto de a e b não é igual a c.")