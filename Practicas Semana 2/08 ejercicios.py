#Inicio
numero = int(input("Ingrese un munero de 4 cifras: "))
#Proceso
d1 = numero % 10
d2= (numero // 10) % 10
d3 = ((numero // 10) // 10) % 10
d4 = (((numero // 10) // 10) // 10) % 10
#Salida
print ("Numero Invertido:",d1,d2,d3,d4)