segundos = float(input("Ingrese la cantidad de Segundos: "))

#Progreso
hora = int(segundos // 3600)
minuto = int(segundos % 3600 // 60)
segundo = int(segundos % 3600 % 60)

#Salida
print("Horas: ",hora)
print("Minutos: ",minuto)
print("Segundos: ",segundo)
