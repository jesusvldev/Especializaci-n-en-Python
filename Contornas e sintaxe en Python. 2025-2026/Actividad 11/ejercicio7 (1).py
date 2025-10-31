""" Crea unha tupla que teña a seguinte estrutura: (Produto, Prezo, Cantidade).
Mostra unha mensaxe de tipo “O produto X costa Y€ e hai Z unidades en stock”.
"""

# Una opción es indexando los valores de la tupla
datos_producto = ('ordenador', 499.99, 15)
print(f'O produto {datos_producto[0]} costa {datos_producto[1]}€ e '
      + f'hai {datos_producto[2]} unidades en stock')

# Otra opción es desempaquetando la tupla:
producto, precio, cantidad = ('ordenador', 499.99, 15)
print(f'O produto {producto} costa {precio}€ e '
      + f'hai {cantidad} unidades en stock')
