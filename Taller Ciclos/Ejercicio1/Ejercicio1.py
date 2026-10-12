#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 1
'''Escribir un programa para el siguiente problema: Un usuario quiere comprar un
helado en una conocida marca de comida rápida y desea saber cuánto le costará en función del
topping que elija. NOTA: Puede escoger o no un topping. Si desea topping, solo puede seleccionar
uno.
'''



# Precios constantes, variables inicializadas
PRECIO_HELADO_BASE = 1.90
PRECIO_TOPPING_FRUTAS = 0.50
PRECIO_TOPPING_GRANOLA = 1.50
PRECIO_TOPPING_OREO = 1.00
PRECIO_TOPPING_BROWNIE = 0.75

# Variables de control
total_a_pagar = 0.0



print(" ¡Bienvenido a la Heladería Placer en tu paladar! \n")

continuar = input(" ¿Deseas realizar una compra?,escribes 'si' y selecciona una opción del menú o 'no' para salir del programa \n") 

# Ciclo principal para procesar uno o varios pedidos
while continuar == "SI" or continuar == "si":
    print("Seleccione la opcion deseada")
    print("--- MENÚ DE TOPPINGS ---")
    print("1. Sin topping   ($1.90)")
    print("2. Frutas        ($0.50)")
    print("3. Granola       ($1.50)")
    print("4. Oreo          ($1.00)")
    print("5. Brownie       ($0.75)")
    
    opcion_sele =int(input("\n Digite el número del topping que deseado: "))
    
    # Evaluación del topping y cálculo del costo del helado actual
    if  opcion_sele  == 1 :
        costo_helado = PRECIO_HELADO_BASE
        print(">> Añadido: Helado tradicional sin topping ($1.90).")
        total_a_pagar += costo_helado
        
    elif  opcion_sele == 2 :
        costo_helado = PRECIO_HELADO_BASE + PRECIO_TOPPING_FRUTAS
        print(f">> Añadido: Helado con Topping de Frutas { costo_helado}.")
        total_a_pagar += costo_helado
        
    elif  opcion_sele == 3 :
        costo_helado = PRECIO_HELADO_BASE + PRECIO_TOPPING_GRANOLA
        print(f">> Añadido: Helado con Topping de Granola {costo_helado}")
        total_a_pagar += costo_helado
        
    elif  opcion_sele == 4 :
        costo_helado = PRECIO_HELADO_BASE + PRECIO_TOPPING_OREO
        print(f">> Añadido: Helado con Topping de Oreo {costo_helado} .")
        total_a_pagar += costo_helado
        
    elif  opcion_sele == 5 :
        costo_helado = PRECIO_HELADO_BASE + PRECIO_TOPPING_BROWNIE
        print(f">> Añadido: Helado con Topping de Brownie {costo_helado}.")
        total_a_pagar += costo_helado
        
    else:
        # Mensaje para cuando el topping no existe en el menú
        print(" Lo sentimos, no contamos con el topping solicitado en nuestro menú.")
        print("   (Este helado no fue añadido a la cuenta).")

    # Preguntar si el usuario desea realizar otro pedido
    print("-" * 45) #usamos para imprimir una linea divisora
    continuar = input("¿Desea agregar otro helado a su pedido? (si/no): ").strip().lower()
    print("-" * 45 + "\n")#usamos para imprimir una linea divisora

# Mensaje con la cuenta total 
print("=================================================")
print("             FACTURA DE SU COMPRA                ")
print("=================================================")
if total_a_pagar > 0:
    print(f" ¡Gracias por su compra! El total a pagar es: ${total_a_pagar:.2f}")
    print(" ¡Que disfrute su(s) helado(s) y tenga un dulce día! ")
else:
    print("Aún no has realizado ningún pedido. ¡Te esperamos pronto, en la Heladeria Plcaer en tu paladar!")
print("=================================================")