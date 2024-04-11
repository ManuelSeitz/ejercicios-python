CESTA_COMPRAS = []

print('Lista de compras'.center(40))
print('Ingrese "salir" para salir.')
while True:
    producto = input('Ingresa un producto para agregar a la cesta: ')
    if producto.lower() == 'salir':
        break
    CESTA_COMPRAS.append(producto)

# Eliminar ultimo elemento
CESTA_COMPRAS.pop()

# Invertir lista
CESTA_COMPRAS.reverse()

print('Lista sin el ultimo elemento e invertida:', CESTA_COMPRAS)
