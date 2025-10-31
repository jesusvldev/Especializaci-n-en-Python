""" Crea un dicionario que almacene un inventario dos seguintes produtos:
- Ordenador: 12
- Smartphone: 20
- Tablet: 5
- Auriculares: 32
Actualiza o dicionario tendo en conta que se venderon 2 auriculares e que se
recibiu un pedido de 10 tablets.
Mostra unha mensaxe indicando o número de auriculares que quedan. """

productos = {
    'Ordenador': 12,
    'Smartphone': 20,
    'Tablet': 5,
    'Auriculares': 32
}

print(productos)

productos['Auriculares'] -= 2
productos['Tablet'] += 10

print(productos)

print(f'Quedan {productos["Auriculares"]} auriculares.')
