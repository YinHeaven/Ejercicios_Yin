


# Definir una función para determinar si los números son pares o impares
def definidor(numero):
    for element in range(numero):
        if element % 2 == 0 and element != 0:
            print(f"{element} es par", end=", ")
        else:
            print(f"{element} es impar", end=", ")

# Llamar a la función con el número 10 

while True:
    try:
        ingreso = int(input("\nIngrese un numero: "))
        definidor(ingreso)
    except ValueError:
        print("Por favor, ingrese un numero valido.")
    
    # Preguntar al usuario si desea realizar otra operación
    repetir = input("\n¿Desea realizar otra operación? (s/n): ").strip().lower()
    if repetir != 's':
        print("Saliendo del programa...")
        break