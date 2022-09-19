##################################################################################################
#                          Ejercicio 1
# Crear un programa que determine si una contraseña en segura o no. Se considera segura 
# si tiene al menos una mayúscula, una minúscula y un número. Se debe utilizar funciones.
##################################################################################################

# Creo la función de validación de contraseña y recibe un parámetro, para pasarle la contraseña
def validaContraseña(contraseña):
    # Preparo variables validadoras si tiene mayúscula, minúscula y número, por defecto las dejo como False
    tieneMayusculas = False
    tieneMinusculas = False
    tieneNumeros = False

    # Creo un ciclo que recorre la contraseña
    for letra in range(len(contraseña)):
        # Valido si letra actual es mayúscula
        if(contraseña[letra].isupper()):
            # De ser así, dejo la variable tieneMayusculas como True
            tieneMayusculas = True

        # Valido si letra actual es minúscula
        if(contraseña[letra].islower()):
            # De ser así, dejo la variable tieneMinusculas como True
            tieneMinusculas = True

        # Valido si letra actual es numérica
        if(contraseña[letra].isnumeric()):
            # De ser así, dejo la variable tieneNumeros como True
            tieneNumeros = True
    
    # Verifico si las tres variables validadoras son verdaderos
    if(tieneMayusculas and tieneMinusculas and tieneNumeros):
        # De ser así, la contraseña es segura e imprimo el mensaje
        print("La contraseña es segura")
    else:
        # En caso contrario, la contraseña no es segura e imprimo el mensaje
        print("La contraseña no es segura")
# Fin Función validaContraseña()

# Solicito la contraseña
contraseña = input("Ingresa una contraseña: ")

# Llamo a la función y le paso la contraseña ingresada
validaContraseña(contraseña)


# Separador de ejercicios
print('############################################################')
##################################################################################################
#                          Ejercicio 2
# Escribir  un  programa  que  lea  números  ingresados  y  luego  devuelva  el  total.  Se  debe 
# desarrollar usando recursión. No se pueden utilizar ciclos. Se ingresar números hasta que 
# el usuario ingrese un espacio. Si el primer input es un espacio, entonces imprime 0.
##################################################################################################

# Creo la función suma que recibe el parametro total
def suma(total):
    # Solicito un número
    num = input("Ingresa un número: ")

    # Valido que el número ingresado sea diferente de espacio
    if(num != " "):
        # Sumo el total con el número ingresado convertido en entero
        total = total + int(num)

        # Imprimo el total
        print('Total: %s' % total)

        # Vuelvo a llamar a la función con el total actual
        suma(total)

    else: # Si se ingresó espacio, muestro el total y nada más, por lo que finaliza la recursión
        print('Total: %s' % total)
# Fin función suma()

# Preparo la variable total
total = 0

# Llamo una primera vez la función suma con el total en cero
suma(total)
        




# Separador de ejercicios
print('############################################################')
##################################################################################################
#                          Ejercicio 3
# Crear una clase llamada “cuenta”.  Al  instanciar  la  clase  se  debe  proveer  el  número  de 
# cuenta, el nombre el titular, saldo inicial, tipo cuenta (ahorro, corriente, inversiones). Crear 
# tres métodos depositar, retirar, obtener balance. Si en la cuenta1  hay un saldo inicial de 
# 10  y  se  hace  un  depósito  de  20  y  un  retiro  de  5,  entonces  al  obtener  el  balance  debe 
# mostrar  un  saldo  de  25.  Imprimir  la  información  con  todos  los  datos  de  usuarios  y 
# balances.
##################################################################################################

# Creo la clase cuenta
class cuenta:
    # Creo el método __init__ para recibir los parámetros necesarios en la clase (y la variable self)
    def __init__(self, numero_cuenta, nombre_titular, saldo_inicial, tipo_cuenta):
        # Asigno en la variable self las variables numero de cuenta, nombre del titular y saldo
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo_inicial

        # Valido si el tipo de cuenta está entre los 3 indicados (ahorro, corriente y inversiones)
        if(tipo_cuenta == 'ahorro' or tipo_cuenta == 'corriente' or tipo_cuenta == 'inversiones'):
            # Si coincide con un tipo de cuenta valido, lo asigno a la variable self
            self.tipo_cuenta = tipo_cuenta
            # Además, creo una variable validadora para usarla más tarde y en este caso la asigno como True
            self.tipo_cuenta_valido = True

        else: # En caso de que el tipo de cuenta no coincida con ninguna de las 3 opciones, asigno la variable validadora como False
            self.tipo_cuenta_valido = False
            # También imprimo el mensaje de que no es valido el tipo de cuenta
            print('Tipo de cuenta no valida')

    # Creo el método depositar, y le paso la variable monto (y la variable self)
    def depositar(self, monto):
        # Hago uso del validador de tipo de cuenta para ejecutar o no el proceso de deposito
        if(self.tipo_cuenta_valido):
            # Imprimo un título separador
            print('#### Depositar ################################')
            # Ejecuto el proceso de deposito sumando el monto al saldo de la cuenta
            self.saldo = self.saldo + monto
            # Imprimo el mensaje de que fue agregado el monto y el número de cuenta correspondiente
            print('Se han agregado $%s a tu cuenta %s' % (monto, self.numero_cuenta))
            print('') # Espacio separador


    def retirar(self, monto):
        # Hago uso del validador de tipo de cuenta para ejecutar o no el proceso de retiro
        if(self.tipo_cuenta_valido):
            # Imprimo un título separador
            print('#### Retirar ################################')
            # Ejecuto el proceso de retiro restando el monto al saldo de la cuenta
            self.saldo = self.saldo - monto
            # Imprimo el mensaje de del monto que fue retirado y el número de cuenta correspondiente
            print('Se han retirado $%s de tu cuenta %s' % (monto, self.numero_cuenta))
            print('') # Espacio separador

    def obtenerBalance(self):
        # Hago uso del validador de tipo de cuenta para ejecutar o no el proceso de obtener balance
        if(self.tipo_cuenta_valido):
            # Imprimo un título separador
            print('#### Obtener Balance ################################')
            # Imprimo el nombre del titular, número de cuenta, tipo de cuenta y el saldo
            print('Nombre Titular: %s' % self.nombre_titular)
            print('Número de Cuenta: %s' % self.numero_cuenta)
            print('Tipo de Cuenta: %s' % self.tipo_cuenta)
            print('Saldo: $%s' % self.saldo)
            print('') # Espacio separador
        
# Llamo a la clase cuenta, y le paso un número de cuenta, nombre del titular, saldo inicial y tipo de cuenta. Además, lo asigno a una variable sesión para continuar usandola.
sesión = cuenta(19978454, 'Luis Cortés', 10, 'corriente')

# Llamo a la clase almacenada en la variable sesión y también al método obtenerBalance para conocer el monto inicial.
sesión.obtenerBalance()

# De la misma forma, llamo al metodo depositar y le paso como parámetro el monto que quiero abonar.
sesión.depositar(20)

# Al igual que la primera vez, llamo al metodo obenerBalance, pero esta vez para conocer el monto luego de depositar.
sesión.obtenerBalance()

# Una vez más, llamo al metodo retirar y le paso el monto que quiero retirar de la cuenta almacenada en la variable sesión.
sesión.retirar(5)

# Y por última vez, llamo al metodo obenerBalance, para ver el monto luego del retiro.
sesión.obtenerBalance()