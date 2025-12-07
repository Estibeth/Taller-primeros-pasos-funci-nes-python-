#********** ZONA DE FUNCION ********#
def capturar_kilometros():
    kilometros=1,000
    return kilometros

def calcular_millas(kilometros):
    millas=(kilometros+(5/8)+10)
    return millas

def imprimir_resultado(resultado_millas):
    print("la convercion de kilometros a milla es:"+str(resultado_millas))

    #********** ZONA DE CODIGO PRINCIPAL *********#

    kilometro=capturar_kilometros()
    millas=calcular_millas(kilometro)
    imprimir=imprimir_resultado(resultado_millas)