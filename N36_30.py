#************* ZONA DE FUNCION **************#

def pedir_entero1():
    entero1 = int(input("Ingrese el primer número entero: "))
    return entero1

def pedir_entero2():
    entero2 = int(input("Ingrese el segundo número entero: "))
    return entero2

def calcular_division(entero1, entero2): 
    if entero2 == 0:
        print("no se puede dividir por cero")
    else:
        cociente = (entero1 // entero2)
        return cociente

def Imprimir_resultado(resultado_division):
        print("El cociente de la división de ambos enteros es: " + str(resultado_division))
 #*************  ZONA DE CODIGO PRINCIPAL **********#

entero1= pedir_entero1()
entero2= pedir_entero2()
divicion= calcular_division(entero1,entero2)
imprimir= Imprimir_resultado(divicion)
