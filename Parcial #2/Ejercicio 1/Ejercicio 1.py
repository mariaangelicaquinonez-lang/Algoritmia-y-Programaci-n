
#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 1

'''
Ejercicio 1
Escriba un programa en Python que procese una lista con las lecturas de voltaje (en Volts)
registradas hora a hora durante un día completo (24 lecturas tomadas en un nodo de subestación).
La lista de datos debe ser definida en el mismo archivo.
El programa debe permitir:
1) Calcular el voltaje promedio del día.
2) Determinar la lectura de voltaje más alta y la más baja.
3) Contar cuántas horas el voltaje estuvo por encima del promedio diario.
Requisito: Diseñe al menos tres funciones independientes: calcular_promedio(lista), obtener_extremos(lista)
y contar_sobre_promedio(lista).

'''


def calcular_promedio(lista):
    """Calcula y retorna el promedio de una lista de valores."""
    if not lista:
        return 0.0
    return sum(lista) / len(lista)


def obtener_extremos(lista):
    """Retorna una tupla con el valor máximo y el mínimo de la lista."""
    if not lista:
        return None, None
    voltaje_max = max(lista)
    voltaje_min = min(lista)
    return voltaje_max, voltaje_min


def contar_sobre_promedio(lista):
    """Cuenta cuántas lecturas superan el promedio diario."""
    promedio = calcular_promedio(lista)
    contador = 0
    for lectura in lista:
        if lectura > promedio:
            contador += 1
    return contador


# --- Programa principal ---
# 24 lecturas de voltaje (en Volts) registradas hora a hora durante un día
lecturas_voltaje = [
    119.5,
    119.2,
    118.8,
    118.5,
    118.9,
    119.4,
    120.1,
    121.0,
    121.8,
    122.3,
    122.5,
    122.1,
    121.9,
    122.4,
    122.0,
    121.5,
    120.8,
    120.2,
    119.7,
    119.3,
    119.0,
    119.4,
    119.6,
    119.8,
]

# Ejecución de las funciones
promedio_dia = calcular_promedio(lecturas_voltaje)
maximo, minimo = obtener_extremos(lecturas_voltaje)
horas_sobre_promedio = contar_sobre_promedio(lecturas_voltaje)

# Muestra los resultados
print(f"Lecturas procesadas: {len(lecturas_voltaje)} horas")
print(f"Voltaje promedio del día: {promedio_dia:.2f} V")
print(f"Lectura más alta: {maximo:.2f} V")
print(f"Lectura más baja: {minimo:.2f} V")
print(f"Horas por encima del promedio: {horas_sobre_promedio} horas")