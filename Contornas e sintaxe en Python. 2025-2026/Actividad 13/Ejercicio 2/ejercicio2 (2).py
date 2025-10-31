import math

radios = [2, 5, 7.5, 10]

# Apartado a)
areas = [math.pi*math.pow(radio, 2) for radio in radios]
diametros = [2*math.pi*radio for radio in radios]

# Apartado b)
datos_columnas = []
for columna in range(len(radios)):
    datos = (radios[columna], areas[columna], diametros[columna])
    datos_columnas.append(datos)
print(datos_columnas)

# Apartado c)
for radio, area, diametro in datos_columnas:
    print(f'Circunferencia con radio {radio} -> Area: {area}, Diametro: {diametro}')