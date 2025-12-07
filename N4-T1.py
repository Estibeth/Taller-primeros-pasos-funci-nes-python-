#*************+codigo central main ***********
suma=0 # se crea la variable global
#print ("digite la cantidad de numeros para sumar:")
#cantidad=int(input()) # estar pendiente de los tipos de variables
for i in range (0,10,2):
    print("digite el numero" + str(i+1)+".")
    numero=int(input())
    suma=suma+numero
    
print("la sumatoria total es:"+ str(suma))