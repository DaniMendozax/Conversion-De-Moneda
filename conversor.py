Menu = """
Bienvenido al conversor de monedas 💰💰🤑

1 - Pesos Colombianos
2 - Pesos argentinos
3 - Pesos Mexicanos
4 - Salir

Elige una opcion: """



while True:
    try:
        opcion = int(input(Menu))
        if opcion == 1:
            dolares = float(input("¿Cuantos dolares tienes?: "))
            valor_peso_colombiano = 4060.79
            peso_Colombiano = dolares * valor_peso_colombiano
            peso_Colombiano = round(peso_Colombiano, 2)
            print("Tienes $ " + str(peso_Colombiano) + " Col")

        elif opcion == 2:
            dolares = float(input("¿Cuantos dolares tienes?: "))
            valor_peso_Argentino = 114.08
            peso_Argentino = dolares * valor_peso_Argentino
            peso_Argentino = round(peso_Argentino, 2)
            print("Tienes $ " + str(peso_Argentino) + " Arg")


        elif opcion == 3:
            dolares = float(input("¿Cuantos dolares tienes?: "))
            valor_peso_Mexicano = 20.16
            peso_Mexicano = dolares * valor_peso_Mexicano
            peso_Mexicano = round(peso_Mexicano, 2)
            print("Tienes $ " + str(peso_Mexicano) + " Mex")

        elif opcion == 4: 
            print("Adios")
            break

        else:
            print("Elija una opcion del menu")

    except:
        print('Ingresa una opcion correcta por favor')



