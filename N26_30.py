#************ ZONA DE FUNCION ***********#
def pedir_numero1():
    numero1 =float(input("Ingrese el numero1:"))
    return numero1

def pedir_numero2():
    numero2 = float(input("Ingrese el numero2:"))
    return numero2

def calcular_numeros(numero1, numero2):
    division = numero1 % numero2
    return division

def imprimir_resultado(resultado_divison):
    print("El resultado del residuo es:",resultado_divison)

#************** ZONA DE CODIGO PRINCIPAL **************#
numero1= pedir_numero1()
numero2=pedir_numero2()
division=calcular_numeros(numero1,numero2)
imprimir=imprimir_resultado(division)