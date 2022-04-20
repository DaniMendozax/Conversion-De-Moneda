from tokenize import PseudoExtras


dolares = input("¿Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_peso_colombiano = 3758.60
peso_Colombiano = dolares * valor_peso_colombiano
peso_Colombiano = round(peso_Colombiano, 2)
peso_Colombiano = str(peso_Colombiano)
print("Tienes $ " + peso_Colombiano + " Col")