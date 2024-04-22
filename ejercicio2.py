def calcular_comision(ventas):
    comision_porcentaje = 0.10  # 10% expresado como fracción
    comision_total = ventas * comision_porcentaje
    return comision_total

sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
ventas_mes = float(input("Ingrese el total de ventas realizadas en el mes: "))

comision_total = calcular_comision(ventas_mes) * 3  # Comisiones por tres ventas
total_mes = sueldo_base + comision_total

print("El total por comisiones por las tres ventas en el mes es: $", round(comision_total, 2))
print("El total que recibirá en el mes es: $", round(total_mes, 2))
