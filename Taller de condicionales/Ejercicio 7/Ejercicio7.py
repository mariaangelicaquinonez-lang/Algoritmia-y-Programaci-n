#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales

#Ejercicio 7
#Crear un programa en el cual al momento de ingresar un número. Si este número es múltiplo de 3 debe se sacar Fizz, 
# si el número es múltiplo de 5 debe de sacar Buzz y en caso de que sea múltiplo de 3 y 5 sacar FizzBuzz

# Solicitar un número entero al usuario
numero = int(input("Ingrese un número entero: "))

# Evaluamos las condiciones usando if, elif y else
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print("No es múltiplo ni de 3 ni de 5")  # Si no es múltiplo ni de 3 ni de 5, muestra el número ingresado