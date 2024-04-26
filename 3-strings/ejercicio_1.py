"""Nuestra Base de Datos se ha quedado dañada por culpa de un formulario,
han llegado emails corruptos. 
Corregir el email como consideres para que sea útil y poder enviarles las novedades 
acerca de los contenidos de BigBayData.com"""

EMAILS = 'misupergmail@gmail-com,otrocorreo@gmail-com,unacuentamas@gmail-com'
emails_separados = EMAILS.replace('-', '.').split(',')
for email in emails_separados:
    print(email)
