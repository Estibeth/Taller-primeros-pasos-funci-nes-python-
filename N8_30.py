#********** ZONA DE FUNCION ***********#

def pedir_datos():
    dolar = float(input("ingrese la cantidad de dinero USD: "))
    return dolar

def capturar_tasa():
    tasa= 0.85
    return tasa

def calcular_cambio(dolar, tasa):
    conversion = (dolar * tasa)
    return conversion

def mostrar_convercion(euros):
    print("los dolares USD ingresados a euros son: " +str (euros))

#********** CODIGO PRINCIPAL ***********#
dolar = pedir_datos()
tasa = capturar_tasa()
conversion = calcular_cambio(dolar, tasa)
resultado = mostrar_convercion(conversion)