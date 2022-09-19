# Construir  un  programa  que  determine  si  dos  palabras  ingresadas  por  el  usuario  son 
# anagramas.
##################################################################################################

# Solicito el ingreso de ambas palabras
palabra1 = input('Ingresa palabra 1: ')
palabra2 = input('Ingresa palabra 2: ')

# Preparo dos listas
lista1 = {}
lista2 = {}

# Validar si ambas palabras tienen la cantidad de letras
if(len(palabra1) == len(palabra2)):
    # Creo ciclos para recorrer la palabra 1
    for i in range(len(palabra1)):
        # Agrego cada letra de la palabra 1 a la lista 1
        lista1[i] = palabra1[i]

    # Creo ciclos para recorrer la palabra 2
    for i in range(len(palabra2)):
        # Agrego cada letra de la palabra 2 a la lista 2
        lista2[i] = palabra2[i]

    # Verifico si la lista 1 ordenada es igual a la lista 2 ordenada
    if(sorted(lista1.values()) == sorted(lista2.values())):
        # Si son, indico que lo son
        print('Son anagramas')
    else:
        # En caso contraro, indico que no lo son.
        print('No son anagramas')
else: # Si tienen diferente cantidad, descarto que sean anagramas
    print('No son anagramas')