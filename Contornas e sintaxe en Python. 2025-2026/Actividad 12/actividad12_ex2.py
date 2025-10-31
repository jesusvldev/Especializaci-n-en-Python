# Función que aplica el IVA a una base imponible
def aplica_iva(base, iva=1.21):
    base = base * iva
    return base


# Solicitamos la base imponible al usuario
base = int(input('Introduce la base imponible de la factura: '))

# Aplicamos el IVA
print(aplica_iva(base))
