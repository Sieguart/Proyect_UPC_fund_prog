#Inicio
unid = int(input("Unidades Iniciales: "))
#Proceso1
perdida1 = unid * 0.05
unidacumulada1 = unid - perdida1
saldo1 = unidacumulada1 + 50
#Proceso2
perdida2 = saldo1 * 0.08
unidacumulada2 = saldo1 - perdida2
saldo2 = unidacumulada2 + 50
#Proceso3
perdida3 = saldo2 * 0.10
unidacumulada3 = saldo2 - perdida3
saldo3 = unidacumulada3 + 50
#Salida
print("Unidades producidas: ",saldo3)