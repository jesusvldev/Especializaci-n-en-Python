""" EJERCICIO COMPLEMENTARIO 4 """

# a)
print('\n*** Apartado a) ***')
equipos = {
    'Madrid FC': ['Jugador1', 'Jugador2', 'Jugador3'],
    'Barcelona FC': ['Jugador4', 'Jugador5'],
    'Valencia FC': ['Jugador6', 'Jugador7', 'Jugador8', 'Jugador9']
}
print(equipos)

# b)
print('\n*** Apartado b) ***')
equipos['Sevilla FC'] = ['Jugador10', 'Jugador11', 'Jugador12']
print(equipos)

# c)
print('\n*** Apartado c) ***')
posicion = equipos['Valencia FC'].index('Jugador8')
jugador8 = equipos['Valencia FC'].pop(posicion)
equipos['Barcelona FC'].append(jugador8)
print(equipos)

# d)
print('\n*** Apartado d) ***')
equipos.pop('Madrid FC')
print(equipos)

# e)
print('\n*** Apartado e) ***')
nombres_equipos = list(equipos.keys())
print(f'Los equipos que quedan son: {nombres_equipos}')

# f)
print('\n*** Apartado f) ***')
num_jugadores = len(equipos['Barcelona FC'])
print(f'El equipo de Barcelona FC tiene {num_jugadores} jugadores.')
