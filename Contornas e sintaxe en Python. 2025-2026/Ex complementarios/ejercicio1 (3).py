""" EJERCICIO COMPLEMENTARIO 1"""

# a)
print('\n*** Apartado a) ***')
personas = [
    ('Alvaro', 12),
    ('Pedro', 7),
    ('Marta', 8),
    ('Carla', 20),
    ('Marcos', 32)
]

personas.append(('Julia', 45))
personas.insert(0, ('Lorenzo', 62))
print(personas)

# b)
print('\n*** Apartado b) ***')
suma_edades = personas[0][1] + personas[1][1] + personas[2][1] + personas[3][1]
media_edad = suma_edades / len(personas)
print(f'La media de edad es {media_edad:.2f} años.')

# c)
print('\n*** Apartado c) ***')
posicion_medio = len(personas) // 2
persona_medio = personas.pop(posicion_medio)
personas.append(persona_medio)
print(personas)

# d)
print('\n*** Apartado d) ***')
nombres = [personas[0][0], personas[1][0], personas[2][0],
           personas[3][0], personas[4][0]]
nombres.sort()
print(nombres)
