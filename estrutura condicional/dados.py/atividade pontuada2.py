import os
os.system('Cls') 


nome = input("digite seu nome :")
sexo = input("digite seu sexo :")
estado_civil = input("digite seu estado civil :")

match sexo and estado_civil:
    case "F":
        input("digite o seu estado civil :")
    case "casada":
       ano_casada = input("informe o ano de casada:")    
       print(f"{nome}, do sexo {sexo} , tem {ano_casada} anos de casada.") 