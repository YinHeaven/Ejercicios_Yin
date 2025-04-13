

texto = str(input("Introduce un texto: "))

def traductor(texto):
    texto = texto.lower()
    texto = texto.replace("a", "4")
    texto = texto.replace("e", "3")
    texto = texto.replace("i", "1")
    texto = texto.replace("o", "0")
    texto = texto.replace("s", "5")
    return texto

print("Texto traducido ", traductor(texto))
input("presiona enter para cerrar... ")