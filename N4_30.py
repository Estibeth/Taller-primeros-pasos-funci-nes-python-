def capturar_radio():
    radio = float (input("digite el radio del cilindro:"))
    return radio

def capturar_base():
    base = float(input("digite la base del cilindro"))
    return base

def capturar_altura():
    altura=float (input("digite la altura del cilindro:"))
    return altura

def analiza_datos(radio,base,altura):
    volumen=(3.1416* radio * base **2* altura)
    return volumen 

def imprimir_resultados(volumen):
    print("el volumen del cilindro es:" + volumen)

radio=capturar_radio()
altura=capturar_altura()
volumen= analiza_datos(radio,altura)
imprimir_resultados(volumen)