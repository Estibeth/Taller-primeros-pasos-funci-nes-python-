#**************** ZONA DE FUNCION *****************#
def pedir_numero():
    numero= float(input("ingrese el numero para calcular el cuadrado:"))
    return numero

def calcular_cuadrado(numero):
    cuadrado=numero * numero
    return cuadrado

def imprimir_resultado(resultado_cuadrado):
    print("el resultado al cuadrado es: ", resultado_cuadrado)

#************** ZONA DE CODIGO PRINCIPAL *************#

numero=pedir_numero()
cuadrado=calcular_cuadrado(numero)
imprimir=imprimir_resultado(cuadrado)