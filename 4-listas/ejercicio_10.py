"""Haz un sistema de ordenamiento de ayudas para tu comunidad. 
La idea es que insertes todos los emails que quieras para, aleatoriamente, ofrecer N ayudas.
El objetivo es tener un sistema justo de ayudas para repartir entre la ciudadanía que se postula. 
Una vez lo tengas, desarrolla un sistema de envío automático por correo."""

from random import randint

EMAILS_POSTULADOS = [
    "manuuseitz@gmail.com",
    "correo@hotmail.com.ar",
    "pablo@gmail.com",
    "juan@yahoo.com",
    "email@gmail.com",
    "unemailcualquiera@gmail.com"
]
LONGITUD_LISTA = len(EMAILS_POSTULADOS) - 1
PERSONAS_AYUDADAS = []

MINIMO_AYUDAS = 1
MAXIMO_AYUDAS = 10 if len(EMAILS_POSTULADOS) > 10 else LONGITUD_LISTA
NUMERO_AYUDAS = randint(MINIMO_AYUDAS, MAXIMO_AYUDAS)

for _ in range(NUMERO_AYUDAS):
    while True:
        PERSONA_AYUDADA = randint(0, LONGITUD_LISTA)
        if EMAILS_POSTULADOS[PERSONA_AYUDADA] not in PERSONAS_AYUDADAS:
            PERSONAS_AYUDADAS.append(EMAILS_POSTULADOS[PERSONA_AYUDADA])
            break

print('Personas elegidas aleatoriamente:')
for correo_persona in PERSONAS_AYUDADAS:
    print(correo_persona)
    print(f'Enviando correo a {correo_persona}...')
    print()
