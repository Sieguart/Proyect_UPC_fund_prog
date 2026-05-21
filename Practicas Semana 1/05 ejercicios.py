#Inicio 
monto = int(input("Ingrese el Monto: "))

#Proceso
billete50 = monto // 50
billete20 = (monto % 50) // 20
billete10 = ((monto % 50) % 20) // 10
moneda5 = (((monto % 50) % 20 ) % 10 ) // 5
moneda2 =((((monto % 50) % 20 ) % 10 ) % 5 ) // 2
moneda1 =(((((monto % 50) % 20 ) % 10 ) % 5 ) % 2 ) // 1

#Salida
print("Billete de 50: ",billete50)
print("Billete de 20: ",billete20)
print("Billete de 10: ",billete10)
print("Moneda de 5: ",moneda5)
print("Moneda de 2: ",moneda2)
print("Moneda de 1: ",moneda1)