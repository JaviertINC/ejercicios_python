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