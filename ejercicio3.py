def calcular_total_con_descuento(total_compra):
    descuento_porcentaje = 0.15  # 15% expresado como fracción
    descuento = total_compra * descuento_porcentaje
    total_con_descuento = total_compra - descuento
    return total_con_descuento

total_compra = float(input("Ingrese el total de la compra: "))

total_con_descuento = calcular_total_con_descuento(total_compra)

print("El monto a pagar finalmente después del descuento es: $", round(total_con_descuento, 2))
