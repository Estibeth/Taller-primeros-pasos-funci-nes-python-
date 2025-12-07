#******************** ZONA DE FUNCION ************#
def pedir_numero1():
    numero1= float(input("ingrese el numero1:"))
    return numero1

def pedir_numero2():
      numero2 = float(input("Ingrese el numero2:"))
      return numero2

def calcular_numeros(numero1, numero2):
    multiplicacion = numero1 * numero2
    return multiplicacion

def imprimir_resultado(resultado_multiplicacion):
    print("El resultado de la multiplicación es:", resultado_multiplicacion)


#*************** ZONA DE CODIGO PRINCIPAL **************#


numero1 = pedir_numero1()

numero2 = pedir_numero2()

multiplicacion = calcular_numeros(numero1, numero2)

resultado = imprimir_resultado(multiplicacion)