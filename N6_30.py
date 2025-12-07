#********** ZONA DE FUNCION ********#
def pedir_radio():
    radio = float (input("digite el radio del cono:"))
    return radio

def pedir_base():
    base=float (input("digite la base del cono:"))
    return base

def pedir_altura():
    altura=float(input("digite la altura del cono:"))
    return altura
    
def calcular_volumen(radio,base,altura):
    volumen=(3.14159*radio *base**2*altura)
    return volumen

def imprimir_resultado(resultado_volumen):
    print("el volumen del cono es:"+ str(resultado_volumen))

#************ ZONA DE  CODIGO PRINCIPAL **************#
    

radio=pedir_radio()
base=pedir_base()
altura=pedir_altura()
volumen=calcular_volumen(radio,base,altura)
imprimir= imprimir_resultado(volumen)