"""Calcula sabiendo el valor de una factura cuanto será el precio final para el cliente.
Por norma general, el IVA aplicado es de un 21%. Sin embargo, en restaurantes es el 10%.
Calcular el precio final según IVA aplicado. Pista: Pide al usuario que tipo de factura es.
"""

tipo_factura = input('Ingresa el tipo de factura: ')
valor_factura = int(input('Ingresa el valor de la factura: '))
if tipo_factura.lower() == 'restaurante':
    DESCUENTO_IVA = 0.9
else:
    DESCUENTO_IVA = 0.79
precio_final = valor_factura * DESCUENTO_IVA
print('El precio final es de', precio_final, 'pesos')
