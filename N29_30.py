#************ ZONA DE FUNCION **************#
def pedir_numero():
    numero=float(input("digite un numero: "))
    return numero 

def calcular_par_impar(numero):
    par_impar=numero % 2 == 0
    return par_impar

def imprimir_resultado(resultado_par_impar):
    print("la determinacion de si es par o impar es: ", resultado_par_impar)

#********** ZONA DE CODIGO PRINCIPAL ***********#

numero=pedir_numero()
par_impar=calcular_par_impar(numero)
imprimir=imprimir_resultado(par_impar)