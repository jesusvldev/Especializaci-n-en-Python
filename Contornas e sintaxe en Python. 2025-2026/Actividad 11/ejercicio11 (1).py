""" Pídelle ao usuario que introduza o seu DNI, nome e idade. Almacena os seus
datos nun dicionario. """

dni = input('Introduce tu DNI: ')
nombre = input('Introduce tu nombre: ')
edad = int(input('Introduce tu edad: '))

datos = {
    'dni': dni,
    'nombre': nombre,
    'edad': edad
}

print(datos['dni'])
print(datos['nombre'])
print(datos['edad'])
