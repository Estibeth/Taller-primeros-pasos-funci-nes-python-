def capturar_radio():
    radio = float (input("digite el radio del cilindro:"))

    return radio
def capturar_altura():
    altura=float (input("digite la altura del cilindro:"))
    return altura

def analiza_datos(radio,altura):
    volumen=3.1416*(radio**2)* altura
    return volumen 

def mostrar_resultados(volumen):
    print("el volumen del cilindro es:"volumen)

    capturar_radio
    capturar_altura
    analiza_datos
    mostrar_resultados