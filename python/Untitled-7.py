suma=0 # se crea la variable global
print("digite la cantidad de numeros para sumar:")
cantidad=int(input())# estar pendiente de los tipos

for i in range(cantidad):
    print("digite el numero" + str(i+1)+":")
    numero=int(input())
    suma=suma+numero