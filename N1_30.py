#*********** ZONA DE FUNCION ***********#
def definir_base():
    base = 15
    return base

def definir_altura():
    altura = 10
    return altura

def calcular_area(base, altura):
    area = (1/4 * base * altura)
    return area

def imprimir_resultado(resultado_area):
    print("el area del triangulo es: "+str(resultado_area))
#*********** ZONA DE CODIGO PRINCIPAL **********#
base= definir_base()
altura=definir_altura()
area=calcular_area(base,altura)
imprimir=imprimir_resultado(area)
    