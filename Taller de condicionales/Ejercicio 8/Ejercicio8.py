#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales

#Ejercicio 8
#Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posiblidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por
#el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado 
# por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.


# Solicitar la elección al usuario
candidato = input("Elija un candidato (A, B o C): ").strip().upper()

# Estructura condicional
if candidato == "A":
    print("Usted ha votado por el partido rojo")
elif candidato == "B":
    print("Usted ha votado por el partido verde")
elif candidato == "C":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")
    