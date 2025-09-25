import random

print('Hola! Soy un generador de contraseñas. Puedo hacer lo siguiente:')
print('1. Generar simultaneamiente cierta cantidad de contraseñas.')
print('2. Generar contraseñas con una determinada cantidad de caracteres.')
# -------------------------------------------
def generar(longitud:int=6):
    '''Devuelve una contraseña generada aleatoriamente en un numero determinado de caracteres.'''
    caracteres = '1234567890qwertyuiopasdfghjklzxcvbnm!"#$%&/()=?¡;:_'
    temp = ''

    for i in range(longitud):
        temp += random.choice(caracteres)

    return temp

while True:
    numero = input('Ingrese la cantidad de caracteres que desea para su contraseña: ')
    numero2 = input('¿Cuántas contraseñas? ')

    try:
        if numero:
            numero = int(numero)
            if numero < 6:
                numero = 6
                print('* La contraseña debe tener al menos 6 caracteres.')
        else:
            numero = random.randint(6,12)
        if numero2:
            numero2 = int(numero2)
        else:
            numero2 = 1
    except Exception:
        pass
    else:
        break

for j in range(numero2):
    print(f'Contraseña #{j + 1}: {generar(numero)}')
