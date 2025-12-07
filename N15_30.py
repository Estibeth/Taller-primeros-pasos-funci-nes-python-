#************ ZONA DE FUCION **********#
def definir_base():
    base = 20
    return base

def definir_altura():
    altura = 15
    return altura

def calcular_volumen(base, altura):
    volumen = (1/4 * base * altura)
    return volumen

def imprimir_resultado(resultado_volumen):
    print("el area de un paralelogramo es: "+str(resultado_volumen))
    
#************ ZONA DE CODIGO PRINCIPAL ***********#
base= definir_base()
altura= definir_altura()
print(base , altura)
volumen= calcular_volumen(base, altura)
imprimir_resultado(volumen)
    
     