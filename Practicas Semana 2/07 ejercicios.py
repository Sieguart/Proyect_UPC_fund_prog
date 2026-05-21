#Inicio
numero = int(input("Ingrese un munero: "))
#Proceso
unid = numero % 10
decena = (numero // 10) % 10
centena = ((numero // 10) // 10) % 10
millar = (((numero // 10) // 10) // 10) % 10
decenamillar = ((((numero // 10) // 10) // 10) // 10) % 10
#Salida
print (" Unidad: ",unid)
print (" Decena: ",decena)
print (" Centena: ",centena)
print (" Millar: ",millar)
print (" Decena de Millar: ",decenamillar)
