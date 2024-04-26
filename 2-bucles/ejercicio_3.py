"""Partiendo de una frase imprimir palabra por palabra y un contador de palabras totales.
"""

frase = input('Ingresa una frase: ')
palabras = frase.split(' ')
CONTADOR_PALABRAS = 0
for palabra in palabras:
    CONTADOR_PALABRAS += 1
    print(palabra)
print('Palabras totales:', CONTADOR_PALABRAS)
