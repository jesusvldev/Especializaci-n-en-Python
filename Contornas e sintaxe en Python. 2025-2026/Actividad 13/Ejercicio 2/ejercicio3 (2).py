import random

# Apartado a)
numeros = [numero for numero in range(1, 51)]
# numeros = list(range(1, 51))

# Apartado b)
carton = random.sample(numeros, 10)

# Apartado c)
bola = random.randint(1, 50)
# bola = random.choice(numeros)

# Apartado d)
if bola in carton:
    print('BINGO!!!')
