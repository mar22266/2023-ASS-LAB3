# Programa de conversiones de binario a hexagecimal y vice versa

while True:
    print("\n")
    print("Menu:")
    print("1. Hexagecimal a Binario")
    print("2. Binario a Hexagecimal 2")
    choice = input("Ingrese el numero de la opcion anterior(1 o 2): ")

    if choice == "1":
        hexa = input("Ingrese un número hexadecimal de 3 dígitos: ")
        bina = bin(int(hexa, 16))[2:].zfill(12)
        print(f"El número binario equivalente es: {bina}")
        break

    elif choice == "2":
        bina = input("Ingrese un número binario de 12 dígitos: ")
        hexa = hex(int(bina, 2))[2:].upper()
        print(f"El número hexadecimal equivalente es: {hexa}")
        break

    else:
        print("Numero invalido intente de nuevo")














