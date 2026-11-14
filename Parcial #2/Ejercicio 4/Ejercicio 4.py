#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 4

'''
Ejercicio 4
Un profesor guarda las notas de sus estudiantes en un diccionario:
notas = {
"Harry": [3.8, 4.0, 4.2],
"Ron": [3.2, 3.8, 2.8],
"Hemione": [5.0, 5.0, 5.0]
"Daco": [4.5, 4.2, 5.0]
"Nevil": [2.5, 3.0, 3.2]
}

Crea funciones que permitan:
1) Calcular el promedio simple de cada estudiante.
2) Calcular un promedio ponderado (30 %, 30 %, 40 %).
3) Determinar quién tiene el mayor promedio final.
4) Mostrar solo los estudiantes aprobados (≥ 3.0).
Bonus: Mostrar mensaje el cual diga quien aprobó o no la clase de la profesora Mcgonagall

'''

def limpiar(n):
  return int(n) if n == int(n) else n


# 1) Calcular el promedio simple de cada estudiante
def calcular_promedio_simple(diccionario):
  promedios = {}
  for estudiante, lista_notas in diccionario.items():
    promedio = sum(lista_notas) / len(lista_notas)
    promedios[estudiante] = limpiar(round(promedio, 2))
  return promedios


# 2) Calcular el promedio ponderado (30 %, 30 %, 40 %) usando ciclo for
def calcular_promedio_ponderado(diccionario, pesos=(0.30, 0.30, 0.40)):
  promedios = {}
  for estudiante, lista_notas in diccionario.items():
    acumulado = 0
    for i in range(len(lista_notas)):
      acumulado += lista_notas[i] * pesos[i]
    promedios[estudiante] = limpiar(round(acumulado, 2))
  return promedios


# 3) Determinar quién tiene el mayor promedio final
def obtener_mayor_promedio(promedios):
  mejor_estudiante = None
  mayor_nota = -1
  for estudiante, promedio in promedios.items():
    if promedio > mayor_nota:
      mayor_nota = promedio
      mejor_estudiante = estudiante
  return mejor_estudiante, mayor_nota


# 4) Mostrar solo los estudiantes aprobados (>= 3.0)
def mostrar_aprobados(promedios, nota_minima=3.0):
  print(f"\n=== ESTUDIANTES APROBADOS (>= {nota_minima}) ===")
  for estudiante, promedio in promedios.items():
    if promedio >= nota_minima:
      print(f"- {estudiante}: {promedio}")


# Bonus: Mensaje indicando quién aprobó o no la clase de la profesora McGonagall
def estado_clase_mcgonagall(promedios, nota_minima=3.0):
  print("\n=== BOLETÍN FINAL - CLASE DE LA PROFESORA MCGONAGALL ===")
  for estudiante, promedio in promedios.items():
    if promedio >= nota_minima:
      print(
          f"[APROBADO] {estudiante} aprobó la clase de la profesora McGonagall"
          f" con {promedio}."
      )
    else:
      print(
          f"[REPROBADO] {estudiante} no aprobó la clase de la profesora"
          f" McGonagall (Nota final: {promedio})."
      )


# --- Programa Principal ---
def ejecutar_sistema_notas():
  notas = {
      "Harry": [3.8, 4.0, 4.2],
      "Ron": [3.2, 3.8, 2.8],
      "Hemione": [5.0, 5.0, 5.0],
      "Daco": [4.5, 4.2, 5.0],
      "Nevil": [2.5, 3.0, 3.2],
  }

  promedios_simples = calcular_promedio_simple(notas)
  promedios_finales = calcular_promedio_ponderado(notas)
  mejor_estudiante, nota_maxima = obtener_mayor_promedio(promedios_finales)

  print("=== PROMEDIOS SIMPLES ===")
  for estudiante, prom in promedios_simples.items():
    print(f"- {estudiante}: {prom}")

  print("\n=== PROMEDIOS PONDERADOS (30% - 30% - 40%) ===")
  for estudiante, prom in promedios_finales.items():
    print(f"- {estudiante}: {prom}")

  print(f"\nMayor promedio final: {mejor_estudiante} con {nota_maxima}")

  mostrar_aprobados(promedios_finales)
  estado_clase_mcgonagall(promedios_finales)


if __name__ == "__main__":
  ejecutar_sistema_notas()