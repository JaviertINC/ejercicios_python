# Calcula la nota de presentación

lab1 = 4.5
lab2 = 7.0
lab3 = 5.5
tarea1 = 6.2
tarea2 = 5.0
tarea3 = 2.1
solemne1 = 1.8
solemne2 = 5.4

promedio_lab = (float(lab1) + float(lab2) + float(lab3)) / 3
promedio_tareas = (float(tarea1) + float(tarea2) + float(tarea3)) / 3

nota_presentacion = (promedio_lab * 0.15) + (promedio_tareas * 0.15) + (solemne1 * 0.35) + (solemne2 * 0.35)

print("La nota de presentación es: %s" % nota_presentacion)