# Escribir  un  programa  que  almacene  palabras  ingresadas  por  el  usuario.  Debe  recibir 
# ingreso  de  palabras  hasta  que  el  usuario  ingrese  tres  asteriscos  ***.  Luego  de  esto,  las 
# palabras se deben mostrar por pantalla una única vez. Es decir que, si el usuario ingresó 
# palabras repetidas, se deben mostrar solo una vez. 
##################################################################################################

#Preparo la variable lista
lista = {}

# Preparo una variable para usarla como indice del ciclo
i = -1

# Creo un ciclo infinito
while True:
    # Solicito una palabra y la almaceno en la variable
    palabra = input('Ingresa una palabra: ')

    #Aumento en uno el indice
    i = i + 1

    #Verifico si la palabra es distinto de los tres asteriscos ***
    if(palabra != "***"):
        # Verifico si la palabra ingresada, ya existe en la lista
        if(palabra in lista.values()):
            # Si existe, no la almaceno y le resto 1 al indice
            i = i - 1
        else:
            # Si no existe, almaceno la palabra en la lista
            lista[i] = palabra

    else: # Si se ingresaron los asteriscos, termino el ciclo
        break

#Imprimo la lista
print(lista)