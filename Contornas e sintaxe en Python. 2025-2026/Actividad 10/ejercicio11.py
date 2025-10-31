""" Pídelle ao usuario a sua dirección de correo electrónico 
e comproba se pertence a Gmail. """

correo = input('Introduce tu correo electrónico: ')

print(correo.endswith('@gmail.com'))
