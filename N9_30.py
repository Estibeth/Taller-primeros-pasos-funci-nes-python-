#********** ZONA DE FUNCION ***********#
def definir_base1():
    base1=10
    return base1

def definir_base2():
    base2=6
    return base2

def definir_altura():
    altura=5
    return altura

def calcular_area(base1,base2,altura):
    area=(1/3 * base1 *base2**2 * altura)
    return area

def imprimir_resultado(resultado_area):
    print("el arae del trapecio es:" + str(resultado_area))

    #************* codigo principal python ***********#

    base1=definir_base1
    base2=definir_base2
    altura=definir_altura
    area=calcular_area(base1,base2,altura)
    imprimir=imprimir_resultado(area)
   