

#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 3

'''
Ejercicio 3

Diseñe un sistema que gestione el inventario de un laboratorio de circuitos eléctricos. Ca-
da componente técnico tiene un nombre, una cantidad en stock y un precio unitario. Utilice un

diccionario donde las claves sean los nombres de los componentes (ejemplo: Resistencia 10k,
Capacitor 100uF).
Implemente las siguientes funciones:
1) agregar_componente(diccionario, nombre, cantidad, precio)
2) eliminar_componente(diccionario, nombre)
3) calcular_valor_total(diccionario)
4) mostrar_inventario(diccionario)

El programa principal debe permitir al usuario actualizar el inventario interactiva o secuencial-
mente y mostrar el valor monetario total almacenado en el laboratorio.
'''
def limpiar(n):
  return int(n) if n == int(n) else n


# 1) Agregar un componente nuevo o actualizar uno existente
def agregar_componente(diccionario, nombre, cantidad, precio):
  nombre = nombre.strip()
  if not nombre:
    raise ValueError("El nombre del componente no puede estar vacío.")
  if cantidad < 0 or precio < 0:
    raise ValueError("La cantidad y el precio no pueden ser negativos.")

  if nombre in diccionario:
    diccionario[nombre]["cantidad"] += cantidad
    diccionario[nombre]["precio"] = limpiar(precio)
    print(
        f"Componente '{nombre}' actualizado (Stock actual:"
        f" {diccionario[nombre]['cantidad']})."
    )
  else:
    diccionario[nombre] = {"cantidad": cantidad, "precio": limpiar(precio)}
    print(f"Componente '{nombre}' agregado al inventario.")


# 2) Eliminar un componente del inventario
def eliminar_componente(diccionario, nombre):
  nombre = nombre.strip()
  if nombre in diccionario:
    del diccionario[nombre]
    print(f"Componente '{nombre}' eliminado correctamente.")
  else:
    print(f"Aviso: El componente '{nombre}' no se encuentra en el inventario.")


# 3) Calcular el valor monetario total almacenado
def calcular_valor_total(diccionario):
  total = 0
  for datos in diccionario.values():
    total += datos["cantidad"] * datos["precio"]
  return limpiar(round(total, 2))


# 4) Mostrar el inventario completo en formato tabular
def mostrar_inventario(diccionario):
  print("\n=== INVENTARIO DEL LABORATORIO DE CIRCUITOS ===")
  if not diccionario:
    print("El inventario está vacío.")
    return

  print(
      f"{'Componente':<22} | {'Stock':>6} | {'P. Unitario':>12} |"
      f" {'Subtotal':>12}"
  )
  print("-" * 60)
  for nombre, datos in diccionario.items():
    cantidad = datos["cantidad"]
    precio = datos["precio"]
    subtotal = limpiar(round(cantidad * precio, 2))
    print(
        f"{nombre:<22} | {cantidad:>6} | ${precio:>11,.2f} | ${subtotal:>11,.2f}"
    )
  print("-" * 60)
  print(f"Valor monetario total: ${calcular_valor_total(diccionario):,.2f}\n")


# --- Programa Principal Interactivo ---
def ejecutar_sistema():
  # Inventario inicial con componentes del ejemplo
  inventario = {
      "Resistencia 10k": {"cantidad": 150, "precio": 50},
      "Capacitor 100uF": {"cantidad": 40, "precio": 350},
      "Protoboard 830 pts": {"cantidad": 12, "precio": 12500},
  }

  while True:
    print("\n--- GESTIÓN DE INVENTARIO ---")
    print("1. Agregar o actualizar componente")
    print("2. Eliminar componente")
    print("3. Mostrar inventario")
    print("4. Calcular valor total")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ").strip()

    if opcion == "1":
      try:
        nombre = input("Nombre del componente (ej. Diodo LED Rojo): ")
        cantidad = int(input("Cantidad a ingresar: "))
        precio = float(input("Precio unitario ($): "))
        agregar_componente(inventario, nombre, cantidad, precio)
      except ValueError as e:
        print(f"Error en los datos ingresados: {e}")

    elif opcion == "2":
      nombre = input("Nombre del componente a eliminar: ")
      eliminar_componente(inventario, nombre)

    elif opcion == "3":
      mostrar_inventario(inventario)
      input("Presiona Enter para volver al menú...")

    elif opcion == "4":
      total = calcular_valor_total(inventario)
      print(f"\nValor monetario total en el laboratorio: ${total:,.2f}")

    elif opcion == "5":
      print("Cerrando sistema de inventario...")
      break
    else:
      print("Opción no válida. Elija un número del 1 al 5.")


if __name__ == "__main__":
  ejecutar_sistema()


