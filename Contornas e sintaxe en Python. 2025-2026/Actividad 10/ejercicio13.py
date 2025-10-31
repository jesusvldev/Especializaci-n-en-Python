""" Pídelle ao usuario unha palabra e comproba se comeza por vogal. """

palabra = input('Introduce una palabra: ')

palabra = palabra.lower()

# empieza_por_vocal = palabra.startswith('a') or palabra.startswith('e') or \
#                     palabra.startswith('i') or palabra.startswith('o') or \
#                     palabra.startswith('u')

empieza_por_vocal = palabra.startswith(('a', 'e', 'i', 'o', 'u'))

print(empieza_por_vocal)
