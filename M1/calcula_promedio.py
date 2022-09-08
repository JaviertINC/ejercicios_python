# Calcula el promedio entre tres notas ingresadas por teclado

nota1 = input("Ingresa la primer nota: ")
nota2 = input("Ingresa la segunda nota: ")
nota3 = input("Ingresa la tercer nota: ")

promedio = (float(nota1) + float(nota2) + float(nota3)) / 3

print("El promedio de las tres notas ingresadas, corresponde a: %s" % promedio)