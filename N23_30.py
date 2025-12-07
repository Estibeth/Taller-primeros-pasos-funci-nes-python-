#*********** ZONA DE FUNCION **********#
def pedir_numero1():
  numero1 = float(input("Ingrese el numero1:"))
  return numero1

def pedir_numero2():
   numero2= float(input("Ingrese el numero2:"))
   return numero2

def calcular_numeros(numero1, numero2):
   suma= numero1 + numero2
   return suma

def imprimir_resultado(resultado_suma):
   print("El resultado de la suma es:", resultado_suma)

#*************** ZONA DE CODIGO PRINCIPAL *********#

numero1= pedir_numero1()
numero2= pedir_numero2()
suma = calcular_numeros(numero1, numero2)
resultado = imprimir_resultado(suma)