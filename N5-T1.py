suma=0 # se crea la variable global
print("digite la cantidad de numeros par sumar:")
cantidad=int(input()) # estar pediente de los tipos

for i in range (cantidad):
    print("digite el numero" + str(i+1)+":")
    numero=int(input())
    suma=suma+numero 
    print("la sumatoria total es :"+ str (suma))