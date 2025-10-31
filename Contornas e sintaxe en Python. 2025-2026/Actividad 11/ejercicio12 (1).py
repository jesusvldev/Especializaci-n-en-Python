""" Crea un dicionario con 5 nomes de frutas e o seu prezo. Móstralle
ao usuario todas as frutas que hai e pregúntalle cal quere comprar e
canta cantidade. Móstralle cal vai ser o prezo total da compra.
Unha vez feito isto, fai un desconto do 10 % sobre o prezo
de todas as frutas. """

frutas = {
    'pera': 2.30,
    'manzana': 1.80,
    'platano': 3.15,
    'naranja': 4.60,
    'cerezas': 7.20
}

nombre_frutas = list(frutas.keys())
# Utilizamos el método join() para eliminar los [] de la lista al imprimir
print(f'Lista de frutas: {', '.join(nombre_frutas)}')


fruta_deseada = input('Indica cuál quieres comprar: ')
cantidad_deseada = int(input('Indica la cantidad que quieres comprar: '))
precio_fruta_deseada = frutas[fruta_deseada]
print(f'El precio total de compra es {precio_fruta_deseada * cantidad_deseada:.2f}€.')

# Hacemos el descuento
for fruta in frutas:
    frutas[fruta] *= 0.9
