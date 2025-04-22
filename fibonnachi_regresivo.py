#fibonachi regresivo
total = 0

def combination(number):
    global total  
    if number > 0: 
        print(number," ", end="")
        total += number
        combination(number - 1)
    


try:
    user_input = int(input("Ingresa un número: "))
    combination(user_input)
    print(f"\nLa suma total de los números es: {total}")
except ValueError:
    print("Por favor, ingresa un número válido.")

input('Presiona Enter para salir...')

