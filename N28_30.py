#************** ZONA DE FUNCION ***********#
def pedir_base():
    base=float(input("ingrese el base del triangulo:"))
    return base

def pedir_altura():
    altura=float(input("ingrese la altura del triangulo:"))
    return altura

def calcular_area(base,altura):
    area= (base * altura) / 2
    return area

def imprimir_resultado(resultado_area):
    print("el resultado del area culculado es: ",resultado_area)
#*********** ZONA DE CODIGO PRINCIPAL ************#
base=pedir_base()
altura=pedir_altura()
area=calcular_area(base,altura)
imprimir=imprimir_resultado(area)
