# Debes crear un programa que dibuje una matriz, según las siguientes consideraciones: 
# 1. Solicitud de filas 
# 2. Solicitud de columnas 
# 3. Se logre dibujar filas indicadas 
# 4. Se logre dibujar columnas solicitadas. 

##################################################################################################

# Solicito el ingreso de Filas y lo convierto a entero
filas = int(input("Ingresa la cantidad de Filas: "))

# Solicito el ingreso de Columnas y lo convierto a entero
columnas = int(input("Ingresa la cantidad de Columnas: "))

# Hago un ciclo for para imprimir la cantidad de filas indicadas
for filas in range(filas):
    # Aquí hago un for para dibujar la parte superior de las columnas hacia al lado.
    for columnas_superior in range(columnas):
        print('+---', end="")
    # Con este pongo el + final para cerrar el dibujo de la parte superior.
    print("+")

    # Aquí hago un for para dibujar la parte central de las columnas hacia al lado.
    for columnas_central in range(columnas):
        print('|   ', end="")
    # Al igual que el + anterior, aquí cierro el dibujo en la parte central de cada cuadrado.
    print("|")

#Y un último for para cerrar el dibujo en la parte inferior.
for columnas_inferior in range(columnas):
    print('+---', end="")
# Y aquí el último + para cerrar el dibujo.
print("+")