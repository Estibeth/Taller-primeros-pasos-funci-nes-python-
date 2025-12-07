#********** ZONA DE FUNCION  **********#
def definir_pi():
    pi=3.14
    return pi

def definir_radio():
    radio=10
    return radio

def definir_altura():
    altura=15
    return altura

def calcular_volumen(pi,radio,altura):
    volumen=(1/3 * pi *radio**2 * altura)
    return volumen 

def imprimir_resultado(resultado_volumen):
    print("el volumen del circulo es:" + str(resultado_volumen))


#********** codigo principal python **********#

pi=definir_pi
radio=definir_radio
altura=definir_altura
volumen=calcular_volumen(pi,radio,altura)
imprimir=imprimir_resultado(volumen)
