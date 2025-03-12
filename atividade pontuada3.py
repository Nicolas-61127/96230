nome = input("digite seu nome:")
sexo = input("digite seu sexo:")
estado_civil = input("digite seu estado civil:")

"f" or "F" 
"M" or "m"

if sexo == "F" or "f" and estado_civil == "casada":
   ano_casada = input("informe o ano de casada:")
   print(f"{nome}, do sexo {sexo} , tem {ano_casada} anos de casada.")
else:
   print(f"{nome} , do sexo {sexo}")   