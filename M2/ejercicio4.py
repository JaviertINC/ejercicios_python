# Escoje 2 palabras del mismo largo en que dos letras iguales no coincidan en la misma posición.
# 1. Escoje las 2 palabras de acuerdo a lo solicitado 
# 2. solicita la frase al usuario 
# 3. reemplaza los valores 
# 4. imprime la nueva frase

##################################################################################################

# Indico instrucciones simples, y solicito ambas palabras.
print("Te pediré 2 palabras, ambas deben tener la misma cantidad de caracteres.")
print("Estas palabras deben tener dos o más letras iguales en diferente posición.")
print("Ejemplo:\nmorena\npelito")
palabra1 = input("Palabra 1: ")
palabra2 = input("Palabra 2: ")

# Solicito el ingreso de una frase a codificar
frase = input("Ahora ingresa la frase que quieres codificar: ")

# Muestro la frase ingresada
print('Frase: ', frase)

# Agrego un pre mensaje indicando que mostraré la frase codificada, con end="" para que quede en la misma linea
print("Frase Codificada: ", end="")

# Creo un ciclo para recorrer la frase letra a letra
for i in range(len(frase)):
    # Creo una variable para saltar la letra si es necesario más adelante, por defecto no saltará
    saltar_letra = "no"

    # Creo otro ciclo para recorrer palabra 1
    for j in range(len(palabra1)):
        # Valido si la letra de la frase coincide con alguna letra de Palabra1
        if(frase[i] == palabra1[j]):
            # Si coinciden, imprimo la letra correspondiente de la Palabra2
            print(palabra2[j], end="")
            # Además habilito el salto de letra, para usarlo más adelante
            saltar_letra = "si"

    # Aquí valido si necesito saltar la letra o no
    if(saltar_letra == "no"):
        # Si no necesito saltar, imprimo la letra de la frase correspondiente.
        print(frase[i], end="")
    # En caso contrario, no imprimo nada, para saltar la letra de la frase y poner la correspondiente de la Palabra2