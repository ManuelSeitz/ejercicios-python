frase = input('Ingresa una frase: ')
palabras = frase.split(' ')
contador = 0
for palabra in palabras:
    contador += 1
    print(palabra)
print('Palabras totales:', contador)
