import os

directorio = 'C:\\Users\\javier\\Desktop'

# Listamos los ficheros del directorio
ficheros = os.listdir(directorio)

# Contamos los ficheros
ficheros_pdf = [fichero for fichero in ficheros if fichero.endswith('.pdf')]
print(f'En el Escritorio hay {len(ficheros_pdf)} ficheros PDF.')

# Ordenamos los ficheros
ficheros_pdf.sort()
print('Los ficheros son los siguientes:')
for fichero in ficheros_pdf:
    print(fichero)
