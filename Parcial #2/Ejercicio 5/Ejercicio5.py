

#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 5

'''
 Ejercicio 5 – Juego de Sintonía e Inspección con Niveles de Dificultad
Cree una simulación interactiva donde el estudiante deba calibrar o adivinar la frecuencia de
resonancia secreta de un filtro (un número entero aleatorio entre 1 y 100 Hz).
El programa debe:
1) Solicitar al usuario el nivel de dificultad: Fácil (10 intentos), Medio (6 intentos), Difícil (3
intentos).
2) Generar la frecuencia aleatoria objetivo.
3) Dar pistas si la frecuencia ingresada es mayor o menor a la frecuencia buscada.
4) Mostrar cuántos intentos le quedan al usuario en cada turno.
Requisito de funciones: elegir_dificultad(), generar_numero(), jugar(intentos).
Bonus: Guarde el historial de partidas (resultado final e intentos requeridos) en una lista o en un
archivo de texto historial_juego.txt.
'''


import random


# 1) Solicitar y validar el nivel de dificultad
def elegir_dificultad():
  while True:
    print("\n=== SELECCIÓN DE NIVEL DE DIFICULTAD ===")
    print("1. Fácil   (10 intentos)")
    print("2. Medio   (6 intentos)")
    print("3. Difícil (3 intentos)")
    opcion = input("Seleccione una opción (1-3): ").strip()

    if opcion == "1":
      return 10
    elif opcion == "2":
      return 6
    elif opcion == "3":
      return 3
    else:
      print("Opción no válida. Por favor ingrese 1, 2 o 3.")


# 2) Generar la frecuencia de resonancia aleatoria (1 a 100 Hz)
def generar_numero():
  return random.randint(1, 100)


# 3) Ejecutar la simulación interactiva de sintonía
def jugar(intentos):
  frecuencia_objetivo = generar_numero()
  intentos_restantes = intentos
  intentos_usados = 0

  print(f"\n--- INICIO DE CALIBRACIÓN ({intentos} intentos disponibles) ---")
  print("Adivine la frecuencia de resonancia secreta del filtro (1 a 100 Hz).")

  while intentos_restantes > 0:
    print(f"\nIntentos restantes: {intentos_restantes}")
    try:
      frecuencia_ingresada = int(input("Ingrese la frecuencia de prueba (Hz): "))
    except ValueError:
      print("Error: Debe ingresar un número entero válido.")
      continue

    if frecuencia_ingresada < 1 or frecuencia_ingresada > 100:
      print("Aviso: La frecuencia debe estar entre 1 y 100 Hz.")
      continue

    intentos_usados += 1
    intentos_restantes -= 1

    if frecuencia_ingresada == frecuencia_objetivo:
      print(
          f"\n¡Sintonía perfecta! La frecuencia secreta era {frecuencia_objetivo} Hz."
      )
      print(f"Calibración lograda en {intentos_usados} intento(s).")
      return (
          f"VICTORIA | Objetivo: {frecuencia_objetivo} Hz |"
          f" Intentos usados: {intentos_usados}/{intentos}"
      )
    elif frecuencia_ingresada < frecuencia_objetivo:
      print("Pista: La frecuencia ingresada es MENOR a la frecuencia buscada.")
    else:
      print("Pista: La frecuencia ingresada es MAYOR a la frecuencia buscada.")

  print(
      f"\nSin intentos restantes. No se logró calibrar el filtro (Era {frecuencia_objetivo} Hz)."
  )
  return (
      f"DERROTA  | Objetivo: {frecuencia_objetivo} Hz |"
      f" Intentos usados: {intentos_usados}/{intentos}"
  )


# Bonus) Guardar el historial en una lista y en el archivo historial_juego.txt
def registrar_partida(historial, resultado):
  historial.append(resultado)
  with open("historial_juego.txt", "a", encoding="utf-8") as archivo:
    archivo.write(resultado + "\n")


# --- Programa Principal ---
def ejecutar_simulacion():
  historial_partidas = []
  print("=== SIMULADOR DE SINTONÍA E INSPECCIÓN DE FILTROS ===")

  while True:
    intentos = elegir_dificultad()
    resultado = jugar(intentos)
    registrar_partida(historial_partidas, resultado)

    repetir = input("\n¿Desea jugar otra partida? (si/no): ").strip().lower()
    if repetir != "s":
      break

  print("\n=== HISTORIAL DE PARTIDAS DE LA SESIÓN ===")
  for i in range(len(historial_partidas)):
    print(f"Partida {i + 1}: {historial_partidas[i]}")
  print("Registros guardados en 'historial_juego.txt'.")


if __name__ == "__main__":
  ejecutar_simulacion()