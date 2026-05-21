#Inicio
prestamo = int(input("Prestamo Inicial: "))
#Año1
interes1 = prestamo * 0.12
saldoacumulado1 = prestamo + interes1
saldo1 = saldoacumulado1 - 2000
#Año2
interes2 = saldo1 * 0.12
saldoacumulado2 = saldo1 + interes2
saldo2 = saldoacumulado2 - 2000
#Año3
interes3 = saldo2 * 0.12
saldoacumulado2 = saldo2 + interes3
saldo3 = saldoacumulado2 - 2000
#Salida
print ("Saldo de Año 1: ",saldo1)
print ("Saldo de Año 2: ",saldo2)
print ("Saldo de Año 3: ",saldo3)
print ("Saldo final: ", (saldo3))
