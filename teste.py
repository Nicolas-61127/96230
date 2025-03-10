altura = float(input("qual a sua altura :"))
sexo = input("qual e o seu sexo :")

match sexo: 
    case "M" :
        peso_ideal = (72.7 * altura) - 58
        print(f"\nPeso ideal: {peso_ideal}")

    case "F" :
        peso_ideal = (68.7 * altura) - 48
        print(f"\nPeso ideal: {peso_ideal}")