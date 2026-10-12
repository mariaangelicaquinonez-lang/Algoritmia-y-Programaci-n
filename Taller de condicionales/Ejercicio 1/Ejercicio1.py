#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales



#ejercicio 1 
#Solicitar al usuario un número que este entre 10 y 50.Si el número es el 30,imprimir "Ganaste un premio" 
# en el caso contrario "Perdiste". ¿Que pasaria si el usuario ingresa -10?


# Solicitamos el número al usuario como número flotante o entero
numero = float(input("Ingrese un número entre 10 y 50: "))

# Evaluamos las condiciones según el enunciado del taller
if numero == 30:
    print("Ganaste un premio")
elif numero < 10 or numero > 50:
    print("El número ingresado está fuera del rango de 10 a 50.")
else:
    print("Perdiste")


 
