import random
import string

def generar_contrasena(numero=True, letras=False, simbolos=False, longitud=16):
    caracteres = (
        (string.digits if numero else "") +
        (string.ascii_letters if letras else "") +
        (string.punctuation if simbolos else "")
    )
    if not caracteres:
        return "Error: Debes seleccionar al menos un tipo de carácter."
    
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

for longitud in longitudes:
    imprimir_contrasena(longitud)

input("Presiona Enter para salir...")

