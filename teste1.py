primeiro_numero = int(input("qual e o  primeiro numero :"))
segundo_numero = int(input("qual e o  segundo numero :"))
nome = input("digite seu nome :")
media = float
media = (primeiro_numero + segundo_numero) / 2

if media >= 9 :
    conceito = "A"
elif media < 7 :
    conceito = "B"
elif media < 6 :
    conceito = "C"
elif media < 4 :
    conceito = "D"
elif media < 2 :
    conceito = "E"

match conceito:
    case "A" | "B" | "C":
        print(f"conceito: {conceito}")
        print("aprovado.")
    case "D" | "E" :
        print(f"conceito: {conceito}")   
        print("reprovado.") 
    case _:
        print("opçao invalida.")    