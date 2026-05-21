#Inicio 
monto = int(input("Ingrese el Monto: "))
denofav = int(input("Ingrese su Denominacion Favorita: "))
montofav = int(input("Ingrese su Monto favorito: "))

#Proceso
b50 = monto // 50
monto = monto % 50
b20 = monto // 20
monto = monto % 20
b10 = monto // 10
monto = monto % 10
m5 = monto // 5
monto = monto % 5
m2 = monto // 2
m1 = monto % 2

#Salida
print("Billete de 50: ",b50)
print("Billete de 20: ",b20)
print("Billete de 10: ",b10)
print("Moneda de 5: ",m5)
print("Moneda de 2: ",m2)
print("Moneda de 1: ",m1)
