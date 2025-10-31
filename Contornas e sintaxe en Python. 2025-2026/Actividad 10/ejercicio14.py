""" Pídelle ao usuario o seu nome e apelidos e devólvelle un nome de usuario 
co seguinte formato: 3 primeiras letras do nome + 
3 primeiras letras do primeiro apelido + 
3 primeiras letras do segundo apelido + lonxitude do nome
 """

nombre_apellidos = input('Introduce tu nombre y apellidos: ')

nombre_apellidos = nombre_apellidos.lower()

nombre, primer_apellido, segundo_apellido = nombre_apellidos.split()

usuario = nombre[:3] + primer_apellido[:3] + segundo_apellido[:3] \
        + str(len(nombre))

print(f'Tu usuario es: {usuario}')
