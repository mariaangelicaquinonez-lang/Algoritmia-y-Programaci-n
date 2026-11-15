


#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 6

'''
Ejercicio 6
Crear una máquina dispensadora la cual pueda:
1) Identificar a través de un diccionario cinco productos, los cuales usarán los nombres de los
productos, dicho diccionario tendrá el producto en cuestión y su respectivo precio.
2) Hacer cobro del producto y leer lo que el usuario ingresa.
3) Verificar si hay que hacer devuelta al usuario o no.
4) Muestre un mensaje en donde diga cual es el producto y cuanto es el valor a devolver si se
debe de devolver.
Bonus: Hacer una función la cual indique si el usuario ingresa un valor menor al solicitado
por el producto.
'''

def limpiar(n):
  return int(n) if n == int(n) else round(n, 2)


# 1) Mostrar el catálogo de cinco productos desde el diccionario
def mostrar_productos(productos):
  print("\n=== MÁQUINA DISPENSADORA - CATÁLOGO DE PRODUCTOS ===")
  for nombre, precio in productos.items():
    print(f"- {nombre}: ${limpiar(precio)}")


# Identificar y seleccionar el producto deseado por su nombre
def seleccionar_producto(productos):
  while True:
    entrada = input(
        "\nIngrese el nombre del producto que desea comprar: "
    ).strip()
    for nombre, precio in productos.items():
      if entrada.lower() == nombre.lower():
        return nombre, precio
    print(
        "Producto no disponible. Escriba exactamente uno de los nombres de la"
        " lista."
    )


# Bonus) Función que indica si el usuario ingresa un valor menor al precio
def verificar_pago_insuficiente(monto_ingresado, precio, producto):
  if monto_ingresado < precio:
    faltante = limpiar(precio - monto_ingresado)
    print(
        f"Aviso (Monto insuficiente): Ingresó ${limpiar(monto_ingresado)},"
        f" pero '{producto}' cuesta ${limpiar(precio)}. Le faltan ${faltante}."
    )
    return True
  return False


# 2) Hacer el cobro del producto y leer el dinero ingresado por el usuario
def procesar_cobro(producto, precio):
  print(
      f"\nProducto seleccionado: {producto} | Valor a pagar: ${limpiar(precio)}"
  )
  while True:
    try:
      monto = float(input("Ingrese el dinero con el que va a pagar: $"))
    except ValueError:
      print("Error: Debe ingresar un valor numérico válido.")
      continue

    if monto <= 0:
      print("Error: El valor ingresado debe ser mayor a cero.")
      continue

    if verificar_pago_insuficiente(monto, precio, producto):
      print("Por favor, ingrese un monto igual o superior al valor del producto.\n")
      continue

    return monto


# 3 y 4) Verificar si hay devuelta y mostrar el mensaje con producto y valor
def entregar_producto_y_devuelta(producto, precio, monto_pagado):
  devuelta = limpiar(monto_pagado - precio)
  print("\n=== RESUMEN DE COMPRA ===")
  if devuelta > 0:
    print(f"Producto dispensado: {producto}")
    print(
        f"Pago recibido: ${limpiar(monto_pagado)} | Valor a devolver:"
        f" ${devuelta}"
    )
  else:
    print(f"Producto dispensado: {producto}")
    print("Pago exacto recibido. No hay que hacer devuelta ($0).")


# --- Programa Principal ---
def ejecutar_maquina_dispensadora():
  productos = {
      "Agua": 2000,
      "Papas": 3500,
      "Galletas": 2500,
      "Gaseosa": 3000,
      "Chocolatina": 1800,
  }

  while True:
    mostrar_productos(productos)
    producto_elegido, precio_producto = seleccionar_producto(productos)
    monto_pagado = procesar_cobro(producto_elegido, precio_producto)
    entregar_producto_y_devuelta(
        producto_elegido, precio_producto, monto_pagado
    )

    otra_compra = input("\n¿Desea comprar otro producto? (si/no): ").strip().lower()
    if otra_compra != "s":
      print("Gracias por su compra.")
      break


if __name__ == "__main__":
  ejecutar_maquina_dispensadora()