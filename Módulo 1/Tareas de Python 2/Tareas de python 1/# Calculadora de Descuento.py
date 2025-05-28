# Calculadora de Descuento
precio = float(input("Introduce el precio del producto: "))
if precio > 100:
    descuento = precio * 0.15
    precio_final = precio - descuento
    print(f"Se aplica un descuento del 15%. El precio final es: ${precio_final}")
else:
    print(f"No se aplica descuento. El precio final es: ${precio}")