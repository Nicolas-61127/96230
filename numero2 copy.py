import os 
os.system("clear")

senha_cadastrada = "123"
login_cadastrada = "Marta"


for i in range(3):
    login = input("digite o login:")
    senha = input("digite a senha:")
    
    if login_cadastrada == login and senha_cadastrada == senha:
       print("Acesso permitido")
       break
    else:
       print("Acesso negado.")

       print("FIM")