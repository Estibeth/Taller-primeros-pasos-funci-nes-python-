#************** ZONA DE FUNCION ************#
def pedir_dinero():
    dinero = float(input("Ingrese la cantidad de dinero para la cuenta:"))
    return dinero
 
def definir_interes():
    interes = 0.05
    return interes

def calcular_total(dinero,  interes):
     tasa =(dinero* interes)
     total =(dinero + tasa)
     return total

def Imprimir_resultado(resultado_interes):
    print("La cantidad de dinero solicitado  es:", str(resultado_interes))

#********ZONA DE CODIGO PRINCIPAL *************#

dinero = pedir_dinero()
interes = definir_interes()
total = calcular_total(dinero, interes)
resultado =Imprimir_resultado(total)