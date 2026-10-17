# Variables acumuladora y de control
total_a_pagar = 0
continuar = "s"

print("--- BIENVENIDO A COMIDAS RÁPIDAS EL RAYO ⚡ ---")

# Ciclo para hacer uno o múltiples pedidos
while continuar == "s":
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
        # Mensaje creativo si la opción no existe
        print("❌ ¡Ese plato no existe en nuestro menú astronómico! Revisa la lista e intenta de nuevo.")
    
    continuar = input("\n¿Desea hacer otro pedido? (s/n): ")

print("\n=================================")
print("TOTAL A PAGAR: $", total_a_pagar)
print("¡Gracias por su compra!")
print("=================================")