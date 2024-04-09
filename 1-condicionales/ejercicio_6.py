tipo_factura = input('Ingresa el tipo de factura: ')
valor_factura = int(input('Ingresa el valor de la factura: '))
if (tipo_factura == 'restaurante'):
    descuento_iva = 0.9
else:
    descuento_iva = 0.79
precio_final = valor_factura * descuento_iva
print(precio_final)
