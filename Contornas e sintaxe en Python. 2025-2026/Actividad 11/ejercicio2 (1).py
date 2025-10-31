# a) Crea unha lista con 10 notas académicas.
notas = [3.25, 10.0, 1.5, 4.5, 4.75, 8.6, 9.1, 3.2, 7.1, 5.3]
print(notas)

# b) Mostra cales son as 3 notas máis altas.
notas.sort()
print(notas[-3:])


# c) Mostra cal é a nota máis baixa.
print(notas[0])

# d) Remplaza as 4 notas máis baixas por unha nota de 5.0.
notas[:4] = [5.0, 5.0, 5.0, 5.0]
print(notas)

# e) Volve ordenalas e borra as 3 notas máis altas.
notas.sort()
del notas[-3:]
print(notas)
