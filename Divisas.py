divisas = {
    "USD":900,
    "ARS":0.99,
}

cantidad = int(input("Cantidad de divisas: "))
simbolo = input("Simbolo divisas: ")

if simbolo not in divisas.keys():
    print("El simbolo no es valido")

else:
    total = divisas[simbolo]*cantidad
    print(f"El total de divisas CLP en {simbolo} es: ", total)