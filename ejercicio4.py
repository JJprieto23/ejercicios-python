def calcular_calificacion_final(calif_parcial1, calif_parcial2, calif_parcial3, calif_examen_final, calif_trabajo_final):
    porcentaje_parciales = 0.55
    porcentaje_examen_final = 0.30
    porcentaje_trabajo_final = 0.15

    promedio_parciales = (calif_parcial1 + calif_parcial2 + calif_parcial3) / 3

    calificacion_final = (promedio_parciales * porcentaje_parciales) + (calif_examen_final * porcentaje_examen_final) + (calif_trabajo_final * porcentaje_trabajo_final)

    return calificacion_final

# Solicitar las calificaciones al usuario
calif_parcial1 = float(input("Ingrese la calificación del primer parcial: "))
calif_parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
calif_parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
calif_examen_final = float(input("Ingrese la calificación del examen final: "))
calif_trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

# Calcular la calificación final
calif_final = calcular_calificacion_final(calif_parcial1, calif_parcial2, calif_parcial3, calif_examen_final, calif_trabajo_final)

print("La calificación final del alumno en la materia de Algoritmos es:", round(calif_final, 2))
