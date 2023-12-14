def calcular_valor(precio):
    bandera = True
    aux = 0

    while bandera:
        bande = False
        while not bande:
            try:
                moneda = int(input("Ingrese la moneda: "))
                if moneda in [10, 50, 100]:
                    bande = True
                else:
                    print("Ingrese una moneda válida.")
            except ValueError:
                print("Ingrese un número válido.")

        aux += moneda
        if aux >= precio:
            bandera = False
       

    return aux

def vueltos(total, precio):
    cambio = total - precio
    aux = cambio / 50

    if int(aux) == 0:
        aux = cambio / 10
        if int(aux) != 0:
            print(f"Su cambio es: {int(aux)} de 10")
        else:
            print("No hay cambio")
    else:
        cM = int(aux)
        cambio -= 50
        aux = cambio / 10
        if int(aux) != 0:
            print(f"Su cambio es: {cM} de 50 y {int(aux)} de 10")
        else:
            print("No hay más cambio")

def maqui_de_comida():
    precio_comida = {1: 270, 2: 340, 3: 390}

    print("Seleccione el producto:")
    for i in range(1, 4):
        print(f"{i}. Producto {i}: {precio_comida[i]}")

    bandera = False
    while not bandera:
        try:
            producto = int(input("Ingrese el número del producto: "))
            if 1 <= producto <= 3:
                bandera = True
            else:
                print("Por favor, ingrese un número del 1 al 3.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    total = calcular_valor(precio_comida[producto])
    vueltos(total, precio_comida[producto])


maqui_de_comida()
