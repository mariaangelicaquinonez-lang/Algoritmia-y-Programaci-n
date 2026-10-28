#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 2

'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si
el cliente es menor de 5 años puede entrar gratis (es decir que el valor de la entrada es $0),
si tiene entre 5 y 18 años debe pagar $5 y si es mayor de 18 años, $10. Para este punto debe:

a) Identificar las entradas y salidas.
b) Hacer el diagrama de flujo que resuelva el problema.
c) Implementar el código del problema.
d) Demostrar el correcto funcionamiento del código. Una prueba puede ser: Suponga que
va a esta sala de juegos y va a entrar usted (ponga su edad) y dos familiares, uno que
tenga 18 años y uno que sea de 4 años.
'''


# Entrada de datos: solicitar la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Estructura condicional para determinar el costo de la entrada
if edad < 5:
    precio = 0
    print(">> Entrada GRATIS ")
elif edad <= 18:
    precio = 5
    print(">> El precio de la entrada es: $5 ")
else:
    precio = 10
    print(">> El precio de la entrada es: $10 ")

print("\n=============================================")
print("\n¡Gracias por su visita a la Sala de Juegos!")
print("\n=============================================")