# Función que borra un usuario de un listín telefónico
def elimina(listin, usuario):
    if usuario in listin:
        del listin[usuario]


# Datos de los usuarios
listin = {'Juan': 123456789, 'Pedro': 987654321}

# Mostramos el usuario eliminado
print(elimina(listin, 'Pablo'))
