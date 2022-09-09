# Cree un programa, donde: 
# 1. Dado el año de nacimiento de una persona 
# 2. El año de muerte 
# 3. Ingresar un cero en caso de estar vivo aún 
# 4. El sistema debe reemplazar el cero por el año actual 
# 5. se determine la cantidad de años bisiestos que le ha tocado vivir. 

##################################################################################################

#Solicito el ingreso de los años de nacimiento y deceso, y los convierto a enteros
año_nacimiento = int(input("Ingresa el año de nacimiento: "))
año_deceso = int(input("Ingresa el año de deceso: "))

# Reemplazo 0 por el año actual
if(año_deceso == 0): año_deceso = 2022

# Creo una variable en 0 para contar los años bisiestos
bisiestos = 0

# Creo un ciclo entre el año de nacimiento y el deceso
for i in range(año_nacimiento, año_deceso):
    # Valido si el año (i) es divisible por 4, y si no es divisible por 100 (siglos) o si es divisible por 400 (siglos divisibles por 400)
    if(i % 4 == 0 and i % 100 != 0 or i % 400 == 0):
        # Agrego 1 al contador de años bisiestos cada vez que se cumple con la condicional de arriba
        bisiestos = bisiestos + 1

# Imprimo los años bisiestos vividos
print('Años bisiestos vividos: ', bisiestos)