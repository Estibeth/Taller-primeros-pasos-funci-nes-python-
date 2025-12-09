#************** ZONA DE FUNCION ***********#
def pedir_longitud():
    longitud=float(input("ingrese el longitud del rectangulo:"))
    return longitud

def pedir_ancho():
    ancho=float(input("ingrese el ancho del rectangulo:"))
    return ancho

def calcular_area(longitud, ancho):
    area= (longitud * ancho) 
    return area

def imprimir_resultado(resultado_area):
    print("el resultado del area del rectangulo  es: ",resultado_area)
#*********** ZONA DE CODIGO PRINCIPAL ************#
longitud=pedir_longitud()
ancho=pedir_ancho()
area=calcular_area(longitud,ancho)
imprimir=imprimir_resultado(area)
