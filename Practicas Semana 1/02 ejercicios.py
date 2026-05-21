#Inicio
horastrabajas = float(input("Sueldo por horas: "))
costohora = float(input("Horas trabajas: "))

#Preceso
sueldobruto = horastrabajas * costohora
bono = (0.1 * sueldobruto)
descuento = (0.05 * sueldobruto)
sueldoneto = sueldobruto + bono - descuento

#Salida
print("El sueldo bruto es: ", sueldobruto)
print("El bono es: ", bono)
print("El descuento es: ", descuento)
print("El sueldo neto es: ", sueldoneto)

