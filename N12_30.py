#************ ZONA DE FUNCION ************#
def definir_pi():
    pi=3.14
    return pi

def definir_lado():
    lado=5
    return lado

def definir_altura():
    altura=5
    return altura

def calcular_volumen(pi,lado,altura):
    volumen =(1/4 * pi *lado**2 * altura)
    return volumen

def imprimir_resultado(resultado_volumen):
    print("el volumen del cuadrado es:"+ str(resultado_volumen))

    #************ ZONA DE CODIGO PRINCIPAL ***********#


    pi= definir_pi
    lado=definir_lado
    altura=definir_altura
    volumen=calcular_volumen(pi,lado,altura)
    imprimir=imprimir_resultado(resultado_volumen)