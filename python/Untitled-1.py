def capturar_usuario():
    nombre_usuario = input("Escriba el nombre del cliente:")
    return nombre_usuario
def capturar_rol():
    rol_usuario = input("escriba su rol:")
    return  rol_usuario
def hacer_saludo(nombre_usuario,rol_usuario):
 mensaje ="Hola " + nombre_usuario + " rol: " + rol_usuario
 return mensaje
def imprimir_mensaje(mensaje):
   print(mensaje)
   #************** zonamde codigo principal **********
   nombre_usuario = capturar_usuario
   rol_usuario = capturar_rol()
   mensaje = hacer_saludo(nombre_usuario, rol_usuario)
   imprimir_mensaje(mensaje)
