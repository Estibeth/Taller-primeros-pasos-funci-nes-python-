#************ZONA DE FUNCION ************#

def capturar_grados():
    grados=33
    return grados

def calcular_fharenheit(grados):
    fahrenheit= (grados+(9/5)+32)
    return fahrenheit

def imprimir_resultado(resultado_fahrenheit):
    print("la conversion de grados celsius a fahrenheit es: " + str(resultado_fahrenheit))

#***********ZONA DE CODIGO PRINCIPAL ************#

grados= capturar_grados()
fharenheit=calcular_fharenheit(grados)
resultado=imprimir_resultado(fharenheit)    


