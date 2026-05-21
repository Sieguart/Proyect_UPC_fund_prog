#Inicio
practica = float(input("Nota de practica: "))
examenparial = float(input("Nota de examen parcial: "))
examenfinal = float(input("Nota de examen final: "))

#Proceso
prompractica = practica * 0.30
promexamenparial = examenparial * 0.30
promexamenfinal = examenfinal * 0.40
promediofinal = prompractica + promexamenfinal + promexamenparial

#Salida
print("Promedio final es: ",promediofinal)
