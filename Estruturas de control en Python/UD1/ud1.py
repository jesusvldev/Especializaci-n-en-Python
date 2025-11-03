nome = input("Introduce teu nome: ")
idade_texto = input("Introduce a túa idade: ")
cidade = input("Introduce a túa cidade favorita: ")

# Non precisamos operar coa idade, así que podería quedar como texto,
# pero se queres validar que é número:
# idade = int(idade_texto)

print(f"Ola, {nome}! Tes {idade_texto} anos e adoras {cidade}.")