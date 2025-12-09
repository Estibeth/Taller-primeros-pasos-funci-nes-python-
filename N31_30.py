#*************** ZONA DE FUNCION ************#
def pedir_hora():
  hora = float(input("Ingrese el numero de hora para convertir a minitos:"))
  return hora

def calcular_minutos(hora):
   minutos= hora * 60
   return minutos

def imprimir_resultado(resultado_minutos):
   print("El resultado de la raiz cuadrada es:", resultado_minutos)

#*************  ZONA DE CODIGO PRINCIPAL **********#
hora=pedir_hora()
minutos=calcular_minutos(hora)
imprimir=imprimir_resultado(minutos)