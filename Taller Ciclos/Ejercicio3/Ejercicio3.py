#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 3

'''Escriba un programa que lea una palabra e imprima todas las subcadenas, ordenadas
por longitud. Por ejemplo, si el usuario introduce “rum”,

'''

# 1. Solicitar la palabra al usuario
palabra = input("Ingrese una palabra: ").strip()

LongitudPalabra = len(palabra)

# 2. Mostrar la palabra ingresada
print("\n" + "=" * 50)
print(f"LA PALABRA INGRESADA POR EL USUARIO ES: '{palabra}' (Longitud: {LongitudPalabra} caracteres)")
print("=" * 50)

print("\n--- SUBCADENAS DIVIDIDAS Y ORDENADAS POR LONGITUD ---\n")


# Controla el tamaño de la subcadena (1, 2, ..., n) dividiendo la palabra segun su tamñano
for tamaño in range(1, LongitudPalabra + 1):
    print(f"Subcadenas de tamaño {tamaño}:")
    
    # Determina la posición inicial dentro de la palabra
    for inicio in range(0, LongitudPalabra - tamaño + 1):
        # Extraer la subcadena usando slicing
        subcadena = palabra[inicio : inicio + tamaño]
        print(f"   --> {subcadena}")
    print()  # Espacio entre grupos de subcadenas

# 5. Resultado final mostrando la palabra completa
print("=" * 50)
print(f" RESULTADO COMPLETO: '{palabra}'")
print("=" * 50)