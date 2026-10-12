#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales

#Ejercicio 4
# Escribir un program que, dadod un numero entero, muestre su valor absoluto. Nota: Para los numeros positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52)
#mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52) NOTA: Para este caso no puede utilizar la funcion abs()



# Solicitar un número entero al usuario
numero = int(input("Ingrese un número entero: "))

# Evaluar si el número es negativo
if numero < 0:
    valor_absoluto = numero * -1
else:
    valor_absoluto = numero

# Mostrar el resultado
print("El valor absoluto es:", valor_absoluto)