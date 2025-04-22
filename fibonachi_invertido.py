# este ejercicio introduce un numero y este cuenta hacia atras hasta llegar a zero y suma el total de todos los numeros
# (es como tratar de hacer combinaciones de todos los numeros y saber el total)

try:
    numero = int(10)
    total = 0

    while numero > 0:
        print(numero)
        total += numero
        numero -= 1

    print(f"La suma total de los números es: {total}")
except ValueError:
    print("Por favor, ingrese un número válido.")
