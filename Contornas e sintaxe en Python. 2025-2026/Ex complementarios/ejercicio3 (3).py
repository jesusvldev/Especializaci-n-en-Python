""" EJERCICIO COMPLEMENTARIO 3"""

import random

# a)
print('\n*** Apartado a) ***')
numero = int(input('Introduce un número: '))
numeros = list(range(1, numero + 1))
print(numeros)

# b)
print('\n*** Apartado b) ***')
rango = list(range(1, 21))
numeros_aleatorios_1 = random.sample(rango, 10)
numeros_aleatorios_2 = random.sample(rango, 10)

# Unimos las listas
numeros_aleatorios = numeros_aleatorios_1 + numeros_aleatorios_2
# Eliminamos duplicados
numeros_aleatorios = list(set(numeros_aleatorios))
print(numeros_aleatorios)

# c)
print('\n*** Apartado c) ***')
nombre = 'javier'
letra = random.choice(nombre)
print(letra)
print(letra in 'aeiou')
