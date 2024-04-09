# Esta es una forma mas realista
import bcrypt

salt = bcrypt.gensalt()
password = 'contraseña'
password_encriptada = bcrypt.hashpw(password.encode(), salt)
password_ingresada = input('Ingresa la contraseña: ')
if password_encriptada == bcrypt.hashpw(password_ingresada.encode(), password_encriptada):
    print('Contraseña correcta, Bienvenido')
else:
    print('Contraseña incorrecta. Acceso denegado.')
