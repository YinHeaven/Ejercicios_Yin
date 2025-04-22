import random
import string

def generar_contrasena(numero=True, letras=False, simbolos=False, longitud= 16):
    caracteres = ""
    
    if numero == True:
        caracteres += string.digits

    if letras == True:
        caracteres += string.ascii_letters 
    
    if simbolos == True:
        caracteres += string.punctuation
    
    if not caracteres:
        return "Error: Debes seleccionar al menos un tipo de carácter."
    
    longitud = random.randint(8, 16)
    if longitud < 8 or longitud > 16:
        return "Error: La longitud de la contraseña debe estar entre 8 y 16."

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitudes = []

longitudes.append(12)
longitudes.append(16) 
longitudes.append(8)
longitudes.append(13)

def imprimir_contrasena(longitud):
    print("Contraseña generada:", generar_contrasena(numero=True, letras=True, simbolos=True, longitud=longitud))

imprimir_contrasena(longitudes[0])
imprimir_contrasena(longitudes[1])
imprimir_contrasena(longitudes[2])
imprimir_contrasena(longitudes[3])

input("Presiona Enter para salir...")

def caracteres():
    return string.digits + string.ascii_letters + string.punctuation


