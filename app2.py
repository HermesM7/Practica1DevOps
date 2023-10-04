import random

letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!#@$%&/?¡*¨_:;"

unir = "{letras}{numeros}{simbolos}"
longitud = 10
contraseña = random.sample(unir, longitud)
print (contraseña)