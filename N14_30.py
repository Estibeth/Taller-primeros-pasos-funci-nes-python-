#*********** ZONA DE FUNCION ***************#
def capturar_pulgadas():
    pulgadas=2.54
    return pulgadas

def calcular_centimetros(pulgadas):
    centimetros=(pulgadas+(3/8)+39)
    return centimetros

def imprimir_resultado(resultado_centimetros):
    print("la convercion de pulgadas a centimetros es: "+ str(resultado_centimetros))


#************ ZONA DE CODIGO PRINCIPAL ***********#


pulgadas=capturar_pulgadas
centimetros=calcular_centimetros(pulgadas)
imprimir=imprimir_resultado(centimetros)