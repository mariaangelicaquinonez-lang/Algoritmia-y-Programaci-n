#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales


#Ejercicio 6
#Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. 
# Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
# informarle que no se puede procesar el dato

# Solicitar el dato al usuario
entrada = input("Ingrese una letra: ").strip()

# 1. Validar que la longitud sea exactamente de 1 carácter
if len(entrada) != 1:
    print("No se puede procesar el dato: debe ingresar exactamente un solo carácter.")
else:
    # Convertir a minúscula para cubrir mayúsculas y minúsculas (ej: 'A' o 'a')
    letra = entrada.lower()
    
    # 2. Evaluar si el carácter es una vocal
    if letra in "aeiouáéíóú":
        print("Es vocal")
    else:
        print("No es una vocal")

