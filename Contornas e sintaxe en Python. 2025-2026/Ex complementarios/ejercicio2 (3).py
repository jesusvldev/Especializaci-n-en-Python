""" EJERCICIO COMPLEMENTARIO 2"""

# a)
print('\n*** Apartado a) ***')
frase = input('Introduce una frase: ')
frase_sin_espacios = frase.replace(' ', '')
print(len(frase_sin_espacios))

# b)
print('\n*** Apartado b) ***')
frase_minusculas = frase.lower()
apariciones_vocales = {
    'a': frase_minusculas.count('a'),
    'e': frase_minusculas.count('e'),
    'i': frase_minusculas.count('i'),
    'o': frase_minusculas.count('o'),
    'u': frase_minusculas.count('u')

}
print(f'La letra "o" aparece {apariciones_vocales['o']} veces.')

# c)
print('\n*** Apartado c) ***')
palabras = frase.split(' ')
ultima_palabra = palabras[-1]
print(ultima_palabra.upper())
print(ultima_palabra.endswith(('a', 'e', 'i', 'o', 'u')))

# d)
print('\n*** Apartado d) ***')
print(frase[::-1])
