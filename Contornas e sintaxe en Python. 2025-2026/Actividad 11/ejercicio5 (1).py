""" Crea unha lista que conteña unha sublista para cada unha das 4 cidades
galegas que son capitais de provincia. En cada sublista, debe aparecer:
• Nome da cidade.
• Número de habitantes.
• Un valor booleano que indique se a cidade ten praia.
Mostra cal é o número medio de habitantes e cantas das cidades teñen praia. """

cidades = [
    ['Lugo', 324346, False],
    ['A Coruña', 23255, True],
    ['Pontevedra', 46095, False],
    ['Ourense', 6576843, False]
]

# Calculamos la media de habitantes
habitantes = [cidade[1] for cidade in cidades]
media_habitantes = sum(habitantes) / len(habitantes)
print(f'El número medio de habitantes es: {media_habitantes}')

# Otra solución válida para hacer el cálculo:
media_habitantes = (cidades[0][1] + cidades[1][1]
                    + cidades[2][1] + cidades[3][1]) / 4

# Mostramos cantas cidades teñen praia
tienen_playa = [cidade[2] for cidade in cidades]
print(f'Hay {sum(tienen_playa)} ciudades con playa.')

# Otra solución válida:
tienen_playa = cidades[0][2] + cidades[1][2] \
                + cidades[2][2] + cidades[3][2]
print(f'Hay {tienen_playa} ciudades con playa.')
