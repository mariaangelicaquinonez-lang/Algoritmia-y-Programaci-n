#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales

#Ejercicio 2
# Solicitar al usuario que ingrese dos numeros y mostrar cual de los dos es menor.
#Dado caso que ambos sean iguales indicar que los dos son iguales.

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num1 < num2:
    menor = num1
elif num2 < num1:
    menor = num2
else:
    menor = None

if menor is not None:
    # Si el decimal es .0, lo convertimos a int para que no imprima el .0
    if menor.is_integer():
        menor = int(menor)
    
    print("El numero menor es:", menor)
else:
    print("Los dos numeros son iguales.")