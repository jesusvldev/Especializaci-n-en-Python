""" Pídelle ao usuario que introduza unha frase e
mostra cantas palabras contén. """

frase = input('Introduce una frase: ')

palabras = frase.split()
print(f'La frase contiene {len(palabras)} palabras.')
