def calcular_interes(capital):
    interes_mensual = 0.02  # 2% expresado como fracción
    interes_ganado = capital * interes_mensual
    return capital + interes_ganado

capital_inicial = float(input("Ingrese el capital inicial: "))
capital_final = calcular_interes(capital_inicial)

print("Después de un mes, el capital final será: $", round(capital_final, 2))
