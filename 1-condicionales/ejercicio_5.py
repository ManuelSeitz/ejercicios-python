puntos = 200
precio_compra = 300
precio_compra_final = precio_compra
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
precio_compra_final = precio_compra * descuento
print(precio_compra_final)
