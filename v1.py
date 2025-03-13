import random
caracteres = "+-_'/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contrs = ''
x = int(input("Escribe la longitud de tu contraseña: "))

if x <= 5:
    while True:
        x = int(input("La longitud es un poco corta. Escribe la longitud de tu contraseña de nuevo: "))
        if x > 5:
            break

for i in range(x):
    carácter_aleatorio = random.choice(caracteres)
    contrs += carácter_aleatorio

print("Contraseña generada:", contrs)