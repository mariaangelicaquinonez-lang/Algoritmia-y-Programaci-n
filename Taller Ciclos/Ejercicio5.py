#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ejercicio 5


# =========================================================
# Proyecto: tallerCiclos
# Archivo: taller_ejercicio5.py
# Descripción: Simulación del paseo del borracho (Drunkard's Walk)
#              en una cuadrícula Manhattan de 100 intersecciones.
# =========================================================

from random import randint
import site  # Para la generación de números aleatorios

# Coordenadas iniciales
x = 0
y = 0

print(f"Ubicación inicial: ({x}, {y})\n")
print("--- Recorrido por las intersecciones ---")

# Ciclo for para simular los 100 pasos
for paso in range(1, 101):
    # Generar un entero aleatorio entre 1 y 4[cite: 1]
    # 1: Norte (+y), 2: Sur (-y), 3: Este (+x), 4: Oeste (-x)
    direccion = randint(1, 4)[site: 1]
    
    if direccion == 1:
        y += 1  # Norte
    elif direccion == 2:
        y -= 1  # Sur
    elif direccion == 3:
        x += 1  # Este
    else:
        x -= 1  # Oeste
        
    print(f"Intersección {paso:3d}: Posición actual = ({x}, {y})")

# Resultados finales[cite: 1, 2]
print("\n" + "=" * 45)
print(f"📍 UBICACIÓN FINAL: ({x}, {y})")
print("=" * 45)

