import random
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
NUMERO_AYUDAS = random.randint(MINIMO_AYUDAS, MAXIMO_AYUDAS)

for _ in range(NUMERO_AYUDAS):
    PERSONA_AYUDADA = random.randint(0, LONGITUD_LISTA)
    if any(
            correo_persona == EMAILS_POSTULADOS[PERSONA_AYUDADA]
            for correo_persona in PERSONAS_AYUDADAS):
        continue
    PERSONAS_AYUDADAS.append(EMAILS_POSTULADOS[PERSONA_AYUDADA])

print('Personas elegidas aleatoriamente:')
for correo_persona in PERSONAS_AYUDADAS:
    print(correo_persona)
    print(f'Enviando correo a {correo_persona}...')
    print()
