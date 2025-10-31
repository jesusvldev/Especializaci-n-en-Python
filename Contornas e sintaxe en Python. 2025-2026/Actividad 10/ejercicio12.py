""" Pídelle unha frase ao usuario e reemplaza todas as 
letras 'a' por '@' e as letras 'o' por '0'. """

frase = input('Introduce una frase: ')
frase = frase.lower()
frase = frase.replace('a', '@').replace('o', '0')
print(frase)
