""" Pídelle ao usuario que introduza unha frase e comproba cantas palabras
aparecen de forma única. Comproba se a palabra “Python” aparece na frase. """

frase = input('Introduce una frase: ')

# Contamos las palabras que aparecen de forma única
palabras = frase.split()
palabras_unicas = set(palabras)
print(f'En la frase aparecen {len(palabras_unicas)} palabras únicas.')

# Comprobamos que 'Python' aparece en la frase
print('Python' in palabras_unicas)
