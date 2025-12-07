# zona de funciones 
def tomar_numero():
    nummero = int(input("escriba el numero:"))
    return nummero

def validar_numero(dato_numero):
    if dato_numero >0:
        mensaje = "el numero es positivo"
    elif dato_numero ==0:
        mensaje = "el numero es nueutro"
    else:
        mensaje =" numero es nagativo"
    return mensaje
def imprimir_numero(dato_mensaje):
    print("el numero es:" + dato_mensaje)

# codigo principal
dato_numero = tomar_numero()
dato_mensaje = validar_numero(dato_numero)
imprimir_numero(dato_mensaje)



