import os 
os.system("clear")

senha_cadastrada = "123"
login_cadastrada = "Marta"


while True:
    login = input("digite o login:")
    senha = input("digite a senha:")
    
    if login_cadastrada == login and senha_cadastrada == senha:
       print("Acesso permitido")
       break
    else:
       print("Acesso negado.")