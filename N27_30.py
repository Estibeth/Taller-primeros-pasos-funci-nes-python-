#*************** ZONA DE FUNCION ************#
def pedir_numero():
  numero = float(input("Ingrese el numero para calcular la raiz cuadrada:"))
  return numero

def calcular_raiz(numero):
   raiz= numero ** 0.5
   return raiz

def imprimir_resultado(resultado_raiz):
   print("El resultado de la raiz cuadrada es:", resultado_raiz)

#*************  ZONA DE CODIGO PRINCIPAL ***********#

numero=pedir_numero()
raiz=calcular_raiz(numero)
imprimir=imprimir_resultado(raiz)