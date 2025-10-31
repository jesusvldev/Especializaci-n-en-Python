# Función que calcula la media de una lista de numeros
def calcular_media(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    media = suma / len(numeros)
    return media


# Lista de datos
datos = [10, 20, 30, 40, 50]

# Cálculo de la media
resultado = calcular_media(datos)
print("La media es: " + str(resultado))
