""" Crea unha lista que conteña 5 tuplas co formato(Nome, Idade).
Mostra cal é a media de idade """

personas = [('Javier', 15), ('Ana', 25), ('Pedro', 43),
            ('Sofía', 67), ('Beatriz', 6)]

# Una opción sería con un bucle
edades = [datos_persona[1] for datos_persona in personas]
media_edad = sum(edades) / len(edades)
print(f'La media de edad es {media_edad:.2f}')

# Otra opción indexando las posiciones
suma_edades = personas[0][1] + personas[1][1] + personas[2][1] \
            + personas[3][1] + personas[4][1]
media_edad = suma_edades / len(personas)
print(f'La media de edad es {media_edad:.2f}')
