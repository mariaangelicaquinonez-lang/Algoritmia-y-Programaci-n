#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 1

'''
Ejercicio 2
Extendiendo la lógica de una calculadora estándar, implemente una calculadora modular basada
en funciones:
1) Implemente las funciones aritméticas básicas: suma(a, b), resta(a, b), multiplicacion(a,
b), division(a, b).

2) Agregue las funciones potencia(base, exponente) y raiz_cuadrada(x), de modo que de-
pendan internamente de la función de multiplicación.

3) Agregue una función factorial(n).
4) Agregue una función inversa(x) que retorne la inversa de un número (1/x, fundamental
para el cálculo de admitancias en circuitos Y = 1/Z).

'''

def limpiar(n):
  return int(n) if n == int(n) else n


# 1) Funciones aritméticas básicas
def suma(a, b):
  return limpiar(a + b)


def resta(a, b):
  return limpiar(a - b)


def multiplicacion(a, b):
  return limpiar(a * b)


def division(a, b):
  if b == 0:
    raise ValueError("Error: No se puede dividir entre cero.")
  return limpiar(a / b)


# 2) Potencia y raíz cuadrada dependientes de multiplicacion()
def potencia(base, exponente):
  base, exponente = limpiar(base), limpiar(exponente)
  if not isinstance(exponente, int):
    raise ValueError("Error: El exponente debe ser entero.")

  resultado = 1
  for _ in range(abs(exponente)):
    resultado = multiplicacion(resultado, base)

  return limpiar(inversa(resultado) if exponente < 0 else resultado)


def raiz_cuadrada(x, tolerancia=1e-7):
  if x < 0:
    raise ValueError(
        "Error: No se puede calcular la raíz cuadrada de un negativo."
    )
  if x == 0:
    return 0

  estimacion = x if x >= 1 else 1.0
  while abs(resta(multiplicacion(estimacion, estimacion), x)) > tolerancia:
    estimacion = multiplicacion(0.5, suma(estimacion, division(x, estimacion)))

  return limpiar(round(estimacion, 7))


# 3) Función factorial
def factorial(n):
  n = limpiar(n)
  if not isinstance(n, int) or n < 0:
    raise ValueError(
        "Error: El factorial solo aplica a enteros mayores o iguales a 0."
    )

  resultado = 1
  for i in range(2, n + 1):
    resultado = multiplicacion(resultado, i)
  return limpiar(resultado)


# 4) Función inversa (1/x, útil para admitancia Y = 1/Z)
def inversa(x):
  if x == 0:
    raise ValueError("Error: La inversa de cero no está definida.")
  return division(1, x)


def ejecutar_calculadora():
  # Cambia estos valores y se actualizarán tanto el texto como el resultado
  a, b = 8, 4
  base, exp = 2, 5
  exp_neg = -3
  num_raiz = 9
  num_fact = 5
  z = 0.25

  print("=== CALCULADORA MODULAR ===")
  print(f"Suma ({a} + {b}): {suma(a, b)}")
  print(f"Resta ({a} - {b}): {resta(a, b)}")
  print(f"Multiplicación ({a} * {b}): {multiplicacion(a, b)}")
  print(f"División ({a} / {b}): {division(a, b)}")
  print(f"Potencia ({base}^{exp}): {potencia(base, exp)}")
  print(f"Potencia negativa ({base}^{exp_neg}): {potencia(base, exp_neg)}")
  print(f"Raíz cuadrada (√{num_raiz}): {raiz_cuadrada(num_raiz)}")
  print(f"Factorial ({num_fact}!): {factorial(num_fact)}")
  print(f"Inversa / Admitancia (Z = {z} Ω -> Y = 1/Z): {inversa(z)} S")

if __name__ == "__main__":
  ejecutar_calculadora()