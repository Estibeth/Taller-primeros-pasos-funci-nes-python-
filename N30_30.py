#************* ZONA DE FUNCION *************#
def pedir_radio():
    radio=float(input("digite el numero del radio del circulo:"))
    return radio

def definir_pi():
    pi=3.14
    return pi

def calcular_circunferencia(radio, pi):
    circunferencia = 2 * pi + radio
    return circunferencia

def imprimir_resultado(resultado_circunferencia):
    print("el resultado del calculo de la circunferencia del circulo es: ", resultado_circunferencia)
#*********** ZONA DE CODIGO PRINCIPAL ***********#
radio=pedir_radio()
pi=definir_pi()
circunferencia=calcular_circunferencia(radio,pi)
imprimir=imprimir_resultado(circunferencia)