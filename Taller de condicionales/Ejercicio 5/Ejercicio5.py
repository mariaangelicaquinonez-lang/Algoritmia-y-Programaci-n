#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales


#Ejercicio 5
#Hacer un programa que permita saber si un año es bisiesto.Para que un año sea bisiesto debe ser divisble por 4 
# y no debe ser divisble por 100, excepto que tambien sea divisible por 400

# Solicitar el año al usuario
año = int(input("Ingrese un año: "))

# Evaluar las condiciones con operadores lógicos and y or
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")