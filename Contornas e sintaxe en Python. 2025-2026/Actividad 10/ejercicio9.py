""" Pídelle ao usuario, por separado, o seu nome e apelidos. 
Móstralle o seu nome e apelidos nunha soa liña, asegurándote de que a 
primeira letra de cada nome e apelido se mostra en maiúscula.
 """

# nombre = input('Introduce tu nombre: ')
# primer_apellido = input('Introduce tu primer apellido: ')
# segundo_apellido = input('Introduce tu segundo apellido: ')

# print(f'El nombre completo es: {nombre.capitalize()} \
# {primer_apellido.capitalize()} {segundo_apellido.capitalize()}.')


nombre = input('Introduce tu nombre: ')
apellidos = input('Introduce tus apellidos: ')

print(f'El nombre completo es: {nombre.capitalize()} {apellidos.title()}')
