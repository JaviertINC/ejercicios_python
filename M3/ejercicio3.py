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