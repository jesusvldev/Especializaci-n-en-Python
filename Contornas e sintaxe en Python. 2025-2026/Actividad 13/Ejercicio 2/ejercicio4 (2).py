from datetime import datetime

vuelos = [
    ('Madrid-París', datetime(2024, 5, 10, 8, 30), datetime(2024, 5, 10, 10, 45)),
    ('París-Nova York', datetime(2024, 5, 11, 14, 15), datetime(2024, 5, 11, 23)),
    ('Nova York-Tokio', datetime(2024, 5, 13, 9), datetime(2024, 5, 14, 11, 30))
]

"""
Si representamos las fechas como strings hay que pasarlas a datetime. Por ejemplo:
    hora_salida = datetime.strptime("2024-5-10 08:30", "%Y-%m-%d %H:%M")
"""

# Apartado a)
for nombre_vuelo, fecha_salida, fecha_llegada in vuelos:
    tiempo_transcurrido = fecha_llegada - fecha_salida
    print(f'El vuelo {nombre_vuelo} duró {tiempo_transcurrido}')

# Apartado b)
trayecto_mas_reciente = max(vuelos, key=lambda vuelo: vuelo[2])
print(f'El trayecto más reciente es {trayecto_mas_reciente[0]}')
