# zona de funcion
def capturar_opcion():
    opcion = input("selecciones una opcion:")
    return opcion

def mostrar_menu():
    while True:
        print("digite la letra A para actualizar sistema")
        print("digite la letra E para eliminar catalago")
        print("digite la letra C para crear productos")
        print("digite la letra S para salir del programa")
        dato= capturar_opcion()
        return dato
    
def validar_opciones(dato_opcion):
        if dato_opcion == 'S' or dato_opcion == 's':
           return"usted escogio salir del programa"
        elif dato_opcion == 'A' or dato_opcion == 'a':
            return "usted escogio actualizar sistema"
        elif dato_opcion == 'E' or dato_opcion == 'e':
           return "usted escogio eliminar catalogo"
        elif dato_opcion == 'C' or dato_opcion == 'c':
          return "usted escogio crear producto"
def imprimir_opcion(dato_mensaje):
        print("usted esta" + dato_mensaje)

        # codigo principal

opcion=capturar_opcion()
menu=mostrar_menu()
opcion=validar_opciones(opcion)
imprimir=imprimir_opcion(opcion)


        
    