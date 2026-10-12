#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales


#Ejercicio 3
#Preguntar al usuario que ingrese un dia de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, 
# otro mensaje diferente si es sabado o domingo.Si el dia ingresado no es ninguno de esos, imprimir otro mensaje 


#Solicitar al Usuario ingresar un dia de la semanana
dia= input("Ingrese un día de la semana: ").strip().lower()

#Estructura condicional

if dia == "lunes":
    print("Inicio de semana! Comenzar al 100%")

elif dia == "viernes":
    print("¡Por fin es Viernes! Sobrevivimos a la semana")

elif dia == "sábado" or dia == "domingo":
    print("Momento de descansar llego el fin de semana" )

else:
    print("Es otro dia de la semana o ingresaste un dato no válido")

