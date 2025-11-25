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
        elif dato_opcion == 'A' or dato_opcional == 'a':
            return "usted escogio actualizar sistema"
        elif dato_opcion == 'E' or dato_opcional == 'e':
           return "usted escogio eliminar catalogo"
        elif dato_opcional == 'C' or dato_opcional == 'c':
          return "usted escogio crear producto"
    def imprimir_opcion(dato_mensaje):
        print("usted esta" + dato_mensaje)

        # codigo principal

        capturar_opcion
        mostrar_menu
        validar_opciones(dato_opcion)
        imprimir_opcion(dato_mensaje)


        
    