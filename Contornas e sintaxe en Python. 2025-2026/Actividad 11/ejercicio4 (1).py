""" Pídelle ao usuario que introduza unha palabra
e comproba se é un palíndromo. """

palabra = input('Introduce una palabra: ')
print(palabra == palabra[::-1])

# Otra opción
lista_letras = list(palabra)
lista_letras.reverse()
print(lista_letras == list(palabra))
