def calcular_porcentaje_genero(estudiantes, hombres, mujeres):
    porcentaje_hombres = (hombres / estudiantes) * 100
    porcentaje_mujeres = (mujeres / estudiantes) * 100
    return porcentaje_hombres, porcentaje_mujeres

# Solicitar información al usuario
estudiantes = int(input("Ingrese el total de estudiantes en el grupo: "))
hombres = int(input("Ingrese el número de hombres en el grupo: "))
mujeres = estudiantes - hombres

# Calcular los porcentajes de hombres y mujeres
porcentaje_hombres, porcentaje_mujeres = calcular_porcentaje_genero(estudiantes, hombres, mujeres)

# Imprimir resultados
print("Porcentaje de hombres en el grupo: {:.2f}%".format(porcentaje_hombres))
print("Porcentaje de mujeres en el grupo: {:.2f}%".format(porcentaje_mujeres))
