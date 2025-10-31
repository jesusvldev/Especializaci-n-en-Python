""" Pídelle ao usuario unha frase e indica cantas 
veces aparece na frase cada letra vogal. """

frase = input('Introduce una frase: ')

# Pasamos todo a minúsculas
frase = frase.lower()

print(f'La letra "a" aparece {frase.count('a')} veces.')
print(f'La letra "e" aparece {frase.count('e')} veces.')
print(f'La letra "i" aparece {frase.count('i')} veces.')
print(f'La letra "o" aparece {frase.count('o')} veces.')
print(f'La letra "u" aparece {frase.count('u')} veces.')


# # Ejemplo con bucle
# frase = input('Introduce una frase: ')
# frase = frase.lower()

# vocales = ['a', 'e', 'i', 'o', 'u']
# for vocal in vocales:
#     print(f'La letra "{vocal}" aparece {frase.count(vocal)} veces.')
