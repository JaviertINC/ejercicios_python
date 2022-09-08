# Crea programa en Python que solicite al usuario: 
# 1. Ingresar un número entero cualquiera del 1 al 9. 
# 2. Luego solicitar que ingrese números secuenciales partiendo por 1,  
# 3. pero saltándose aquellos que sean múltiplos del valor ingresado al comienzo.  
# 4. En caso de ingresar un valor erróneo,  
# 5. enviar un mensaje indicando el error y  
# 6. El número que correspondía ingresar. 

##################################################################################################

# Solicito un número secuencial y lo convierto a entero.
num1 = int(input("Ingresa un número para comenzar el juego: "))

# Valido que el número ingresado esté en el rango de 1 a 9
if(num1 >= 1 and num1 <= 9):
    # Si está en el rango comienzo un ciclo infinito
    while True:
        # Solicito un número secuencial y lo convierto a entero.
        num2 = int(input("Ingresa un número secuencial, que no sea múltiplo de %s: " % (num1)))

        # Valido si el número ingresado es múltiplo del número principal
        if( num2 % num1 != 0):
            # Si está bien, te felicito y seguimos jugando
            print("¡Bien!") 
        else:
            # Si está mal, te lo digo
            # Y te indico cuál es el número que debías ingresar sumando 1 al número que ingresaste
            print("%s es múltiplo de %s, debías ingresar %s :(" % (num2, num1, num2 + 1))
            # Además termino el ciclo usando break
            break
else:
    # Si no está en rango indicado, le muestro el mensaje
    print('El número ingresado no es está en el rengo de 1 a 9')