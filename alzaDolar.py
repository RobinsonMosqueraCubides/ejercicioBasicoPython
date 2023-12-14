def orden(precio, dias):
    aux = 0

    for i in range(1, dias - 1):
        print(f"Día {i}: {precio[i]}")
        aux1 = precio[i] - precio[i + 1]
        if aux1 > aux:
            aux = aux1

    if aux == 0:
        print("No hubo alza")
    else:
        print(f"El alza mayor fue: {aux}")

def alzaDolar():
    bandera = True
    while bandera:
        try:
            dias = int(input("Ingrese el número de días:\n"))
            precio = [0] * dias
            bandera = False
        except ValueError:
            print("Por favor, ingresa un número válido.")
            bandera = True

    for i in range(dias):
        precio[i] = float(input(f"Ingrese el valor del día {i + 1}:\n"))

    orden(precio, dias)

# Llamada a la función principal
alzaDolar()
