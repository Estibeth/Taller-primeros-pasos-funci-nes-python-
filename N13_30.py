#************ ZONA DE FUNCION ***********#
def pedir_longitud():
    longitud=float(input("digite la longitud de la piramide"))
    return longitud

def pedir_ancho():
    ancho=float(input("digite el ancho del piramide"))
    return ancho

def pedir_altura():
    altura=float(input("digite la altura de la piramide"))
    return altura

def calcular_volumen(longitud,ancho,altura):
    volumen=(1/3*longitud *ancho**2 * altura)
    return volumen

def imprimir_resultado(resultado_volumen):
    input("el volumen de la piramide es:"+ str(resultado_volumen))

#************ ZONA DE CODIGO PRINCIPAL *************#

longitud=pedir_longitud
ancho=pedir_ancho
altura=pedir_altura
volumen=calcular_volumen(longitud,ancho,altura)
imprimir=imprimir_resultado(volumen)