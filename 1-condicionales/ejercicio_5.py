"""Imaginemos que en nuestra tienda hay un carné por puntos y que alguien debe pagar
el precio_final_de_compra. 
Si tienes menos de 100 puntos realizaremos un descuento del 10%. 
Si es mayor a 100 y menor a 150 aplicamos un 12%. Si tienes 150 un 15% y sino,
el resto de los casos de más de 150, un 20%."""

puntos = int(input('Ingresa tus puntos: '))
PRECIO_COMPRA = 300
PRECIO_COMPRA_FINAL = PRECIO_COMPRA
# Descuento 10%
if puntos <= 100:
    descuento = 0.9
# Descuento 12%
elif puntos < 150:
    descuento = 0.88
# Descuento 15%
elif puntos == 150:
    descuento = 0.85
# Descuento 20%
else:
    descuento = 0.80
PRECIO_COMPRA_FINAL = PRECIO_COMPRA * descuento
print('El precio de compra final es de:', PRECIO_COMPRA_FINAL)
