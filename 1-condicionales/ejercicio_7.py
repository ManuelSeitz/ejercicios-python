"""Guarda una contraseña como password. 
Crea un sistema de seguridad donde el ordenador muestra un mensaje 
'Ordenador bloqueado. Contraseña incorrecta.' si el usuario falla la contraseña.
En caso contrario, que muestre por pantalla 'Bienvenid@...'."""

import bcrypt

salt = bcrypt.gensalt()
PASSWORD = 'contraseña123'
password_encriptada = bcrypt.hashpw(PASSWORD.encode(), salt)
password_ingresada = input('Ingresa la contraseña: ')
if password_encriptada == bcrypt.hashpw(password_ingresada.encode(), password_encriptada):
    print('Contraseña correcta, Bienvenido')
else:
    print('Contraseña incorrecta. Acceso denegado.')
