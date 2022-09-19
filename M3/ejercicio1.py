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