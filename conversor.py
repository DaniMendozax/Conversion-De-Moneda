Menu = """
Bienvenido al conversor de monedas 💰💰

1 - Pesos Colombianos
2 - Pesos argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(Menu))
if opcion == 1:
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso_colombiano = 3758.60
    peso_Colombiano = dolares * valor_peso_colombiano
    peso_Colombiano = round(peso_Colombiano, 2)
    peso_Colombiano = str(peso_Colombiano)
    print("Tienes $ " + peso_Colombiano + " Col")
elif opcion == 2:
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso_Argentino = 114.08
    peso_Argentino = dolares * valor_peso_Argentino
    peso_Argentino = round(peso_Argentino, 2)
    peso_Argentino = str(valor_peso_Argentino)
    print("Tienes $ " + peso_Argentino + " Arg")

elif opcion == 3:
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso_Mexicano = 20.16
    peso_Mexicano = dolares * valor_peso_Mexicano
    peso_Mexicano = round(peso_Mexicano, 2)
    peso_Mexicano = str(peso_Mexicano)
    print("Tienes $ " + peso_Mexicano + " Mex")

else:
    print('Ingresa una opcion correcta por favor')



