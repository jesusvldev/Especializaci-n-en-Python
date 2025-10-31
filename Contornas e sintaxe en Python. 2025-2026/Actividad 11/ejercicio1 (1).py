# a) Crea a seguinte lista da compra: “pan”, “leite”, “ovos”
lista_compra = ['pan', 'leite', 'ovos']

# b) Engade á lista da compra(nunha única instrución) os alimentos “arroz” e
#     “pasta”.
lista_compra.extend(['arroz', 'pasta'])
# lista_compra += ['arroz', 'pasta']
print(lista_compra)

# c) Engade “auga” ao comezo da lista.
lista_compra.insert(0, 'auga')
print(lista_compra)

# d) Borra os “ovos” da lista.
lista_compra.remove('ovos')
print(lista_compra)

# e) Mostra a posición que ocupan o “leite” na lista.
print(lista_compra.index('leite'))
