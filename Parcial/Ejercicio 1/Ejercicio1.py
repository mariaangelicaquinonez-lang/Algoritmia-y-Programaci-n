#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 1

'''En una franquicia de comida rápida se necesita implementar un sistema con el cual se pueda
hacer uno o múltiples pedidos. NOTA: Diseñe como mínimo cinco opciones y el menú debe
tener precios razonables para los usuarios.
En caso que el usuario pida algo que no haga parte del menú, sacar un mensaje en donde se
le informe que no hay el pedido y volverle a preguntar. NOTA: Sea creativo con el mensaje
que le va a mostrar al usuario. Para este punto debe:

a) Identificar las entradas y salidas.
b) Hacer el diagrama de flujo que resuelva el problema.
c) Implementar el código del problema.
d) Demostrar el correcto funcionamiento del código. Una prueba puede ser: Imagine que
va a almorzar usted junto con su pareja la cual va a pedir un plato de los que hay en el
menú y su sobrino, que no alcanza a leer las opciones, pide algo que no esta en la lista.
'''



# Variables acumuladora y de control
total_a_pagar = 0

print("--- BIENVENIDO A COMIDAS RÁPIDAS EL PUERTO ---")

continuar = input(" ¿Deseas realizar una compra?,escribes 'si' y selecciona una opción del menú o 'no' para salir del programa \n") 

# Ciclo para hacer uno o múltiples pedidos
while continuar == "si":
    print("\n--- MENÚ ---")
    print("1. Combo Hamburguesa - $15000")
    print("2. Perro Caliente    - $12000")
    print("3. Salchipapa        - $10000")
    print("4. Papas Fritas      - $6000")
    print("5. Gaseosa           - $4000")
    
    opcion = input("Ingrese el número del producto que desea pedir: ")
    
    if opcion == "1":
        total_a_pagar = total_a_pagar + 15000
        print(">> Añadido: Combo Hamburguesa ($15000)")
    elif opcion == "2":
        total_a_pagar = total_a_pagar + 12000
        print(">> Añadido: Perro Caliente ($12000)")
    elif opcion == "3":
        total_a_pagar = total_a_pagar + 10000
        print(">> Añadido: Salchipapa ($10000)")
    elif opcion == "4":
        total_a_pagar = total_a_pagar + 6000
        print(">> Añadido: Papas Fritas ($6000)")
    elif opcion == "5":
        total_a_pagar = total_a_pagar + 4000
        print(">> Añadido: Gaseosa ($4000)")
    else:
        # Mensaje si la opción no existe
        print("¡Ese plato no existe en nuestro menú! Revisa la lista e intenta de nuevo.")
    
    continuar = input("\n¿Desea hacer otro pedido? (si/no): ")

print("\n=================================")
print("TOTAL A PAGAR: $", total_a_pagar)
print("¡Gracias por su compra!")
print("=================================")