# Ingresa un rut y calcula el digito verificador

rut = input("Ingresa un rut sin puntos ni digito verificador (8 digitos): ")

print("El rut ingresado es: %s" % rut)

parts_8 = int(rut[7]) * 2
#print("%s * 2 = %s" % (rut[7], parts_8))

parts_7 = int(rut[6]) * 3
#print("%s * 3 = %s" % (rut[6], parts_7))

parts_6 = int(rut[5]) * 4
#print("%s * 4 = %s" % (rut[5], parts_6))

parts_5 = int(rut[4]) * 5
#print("%s * 5 = %s" % (rut[4], parts_5))

parts_4 = int(rut[3]) * 6
#print("%s * 6 = %s" % (rut[3], parts_4))

parts_3 = int(rut[2]) * 7
#print("%s * 7 = %s" % (rut[2], parts_3))

parts_2 = int(rut[1]) * 2
#print("%s * 2 = %s" % (rut[1], parts_2))

parts_1 = int(rut[0]) * 3
#print("%s * 3 = %s" % (rut[0], parts_1))

suma = parts_1 + parts_2 + parts_3 + parts_4 + parts_5 + parts_6 + parts_7 + parts_8
#print("Suma: %s" % suma)

resto = suma / 11
#print("Resto: %s" % int(resto))

once_natural = 11 * int(resto)
#print("OnceNatural: %s" % once_natural)

resto = suma - once_natural
#print("Resto: %s" % int(resto))

dv = 11 - resto
print("Digito verificador: %s" % dv)