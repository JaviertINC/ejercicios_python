##################################################################################################
#                          Ejercicio 1
# Escribir  un  programa  que  lea  entre  10  a  20  números  ingresados  por  el  usuario,
# los almacene en una lista y los muestre ordenados de mayor o menor. Debe recibir el ingreso 
# de números hasta que el usuario ingrese 0. Pero el 0 no se debe mostrar en pantalla.  
##################################################################################################

#Preparo la variable lista
lista = {}
#Preparo una variable para que el usuario ingrese minimo 10 números
minimo = 10

# Creo un ciclo para solicitar los números la cantidad deseada
for i in range(20):
    #Solicito el número y los convierto a entero para manipularlos como números
    num = int(input('Ingresa un número: '))

    #Verifico si el número ingresado es diferente de cero
    if(num != 0):
        # Almaceno el número ingresado en la lista
        lista[i] = num
    else: # Si el número ingresado es cero
        # Valido si ha ingresado al menos 10 numeros
        if(i > 10):
            #Si ingresó 10 o más números, termino el ciclo
            break
        else:# Si no, indico que se debe ingresar minimo 10 números
            print("Ingresa minimo 10 números")

# Uso la función sorted para ordenar los valores de la lista, y con la opción reverse habilitada, qudarán ordenadas de mayor a menor
lista_ordenanda = sorted(lista.values(), reverse=True)

#Imprimo la lista ordenada de mayor a menor
print(lista_ordenanda)






# Separador de ejercicios
print('############################################################')
##################################################################################################
#                          Ejercicio 2
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






# Separador de ejercicios
print('############################################################')
##################################################################################################
#                          Ejercicio 3
# ¡Juguemos Scrabble! 
# Construir un diccionario con los siguientes valores. Luego, el usuario ingresa una palabra 
# por pantalla, y el programa devuelve el puntaje. 
##################################################################################################

# Creo el diccionario
diccionario = {}

# Asigno las letras a los ditstintos valores
diccionario[ 1] = 'A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'
diccionario[ 2] = 'D', 'G'
diccionario[ 3] = 'B', 'C', 'M', 'P'
diccionario[ 4] = 'F', 'H', 'V', 'W', 'Y'
diccionario[ 5] = 'K'
diccionario[ 8] = 'J', 'X'
diccionario[10] = 'Q', 'Z'

# Preparo la variable puntaje total
puntaje_total = 0

# Solicito la palabra para jugar
palabra = input('Ingresa una palabra: ')

# Convierto la palabra en mayúsculas
palabra = palabra.upper()

# Creo un ciclo que recorre la palabra
for i in range(len(palabra)):
    # Preparo la variable puntaje para asignar el puntaje de cada letra
    puntaje = 0

    # Verifico si la letra existe en el diccionario 1
    if(palabra[i] in diccionario[1]):
        # Asigno el puntaje correspondiente
        puntaje += 1

    # Verifico si la letra existe en el diccionario 2
    if(palabra[i] in diccionario[2]):
        # Asigno el puntaje correspondiente
        puntaje += 2
    
    # Verifico si la letra existe en el diccionario 3
    if(palabra[i] in diccionario[3]):
        # Asigno el puntaje correspondiente
        puntaje += 3
    
    # Verifico si la letra existe en el diccionario 4
    if(palabra[i] in diccionario[4]):
        # Asigno el puntaje correspondiente
        puntaje += 2
    
    # Verifico si la letra existe en el diccionario 5
    if(palabra[i] in diccionario[5]):
        # Asigno el puntaje correspondiente
        puntaje += 5

    # Verifico si la letra existe en el diccionario 8
    if(palabra[i] in diccionario[8]):
        # Asigno el puntaje correspondiente
        puntaje += 8

    # Verifico si la letra existe en el diccionario 10
    if(palabra[i] in diccionario[10]):
        # Asigno el puntaje correspondiente
        puntaje += 10
    
    # Imprimo la letra y el puntaje otorgado, para más claridad.
    print('Letra: %s | Puntaje: %s' % (palabra[i], puntaje))

    #Sumo el puntaje de la letra al puntaje total
    puntaje_total = puntaje_total + puntaje

#Imprimo el puntaje total obtenido
print('Puntaje total: %s' % puntaje_total)







# Separador de ejercicios
print('############################################################')
##################################################################################################
#                          Ejercicio 4
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







# Separador de ejercicios
print('############################################################')
##################################################################################################
#                          Ejercicio 5
# Construir un programa en donde el usuario ingrese número por pantalla  y el programa
# devuelva  la  suma  de  cada  número  ingresado  por  el  usuario.  Si  el  usuario  ingresa  un 
# carácter no numérico, debe mostrar mensaje de error y continuar solicitando números y 
# sumando. El programa finaliza cuando usuario presiona enter con espacio en blanco.
##################################################################################################

# Preparo la variable suma
suma = 0

# Creo un ciclo infinito
while True:
    # Intento ejecutar el código
    try:
        # Solicito el ingreso de un número y lo convierto a entero
        num = input('Ingresa el número a sumar: ')
        
        # Valido si num no se ingresó en blanco
        if(num != ''):
            # Sumo el total con el numero ingresado convertido a entero
            suma = suma + int(num)
            # Imprimo la suma total
            print('Suma: %s' % suma)
        else: # Si se ingresó en blanco
            # Muestro el total sumado
            print('Total: %s' % suma)
            # Y termino el ciclo
            break
    # Si el intento falla por ingreso de un valor no numerico
    except ValueError:
        # Muestro error e indico que debe ingresar solo números
        print("[Error] Solo debes ingresar números")