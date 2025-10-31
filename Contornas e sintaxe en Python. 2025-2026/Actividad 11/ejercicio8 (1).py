""" Un restaurante recibe reservas tanto por chamada de teléfono coma por
WhatsApp. Crea unha lista de reservas co nome de 6 persoas que reservaron por
teléfono e outra lista co nome de 6 persoas que reservaron por WhatsApp. Pode
ser que algunha persoa reservara polos dous medios e o seu nome apareza
duplicado.
Elimina os duplicados e garda a lista real de persoas que fixeron unha reserva.
"""

reservas_telefono = ['Javier', 'Paula', 'Bárbara',
                     'Marcos', 'Luis', 'Lucía']
reservas_whatsapp = ['Javier', 'Alejandro', 'Marcos',
                     'Alicia', 'Sofia', 'Paula']

reservas_totales = reservas_telefono + reservas_whatsapp
# Utilizamos un conjunto para eliminar duplicados
reservas_unicas = list(set(reservas_totales))
print(reservas_unicas)
