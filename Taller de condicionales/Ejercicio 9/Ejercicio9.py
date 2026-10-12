#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#taller_Diagramas de flujo y condicionales

#Ejercicio 9
# Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y
#cada nivel tiene clases en un día de la semana diferente: los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes
#se dicta inglés para viajeros. Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día, DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
#número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error.
#Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico],
#[numérico]/[numérico]>. Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya
#que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje
#de aprobados. Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará “asistió la mayoría” en caso de que la
#asistencia sea mayor al 50 % o “no asistió la mayoría” si no es así. Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir “Comienzo de
#nuevo ciclo” y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.



# Solicitud de la fecha
entrada_fecha = input("Ingrese la fecha (ejemplo: lunes, 15/03): ").strip().lower()

# Separación de día y fecha numérica
partes = entrada_fecha.split(",")
dia_semana = partes[0].strip()
fecha_num = partes[1].strip()

# Extracción de día (DD) y mes (MM)
partes_fecha = fecha_num.split("/")
dia_num = int(partes_fecha[0])
mes_num = int(partes_fecha[1])

# Días válidos de la semana
dias_validos = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"]

# Validaciones principales de rango y día
if dia_semana not in dias_validos or dia_num < 1 or dia_num > 31 or mes_num < 1 or mes_num > 12:
    print("Se produjo un error: Se ingresó un día de la semana inexistente o valores de fecha fuera de rango.")
else:
    # 1. Niveles Inicial, Intermedio y Avanzado (Lunes, Martes, Miércoles)
    if dia_semana in ["lunes", "martes", "miércoles", "miercoles"]:
        tomaron_examenes = input("¿Se tomaron exámenes el día de hoy? (sí/no): ").strip().lower()
        if tomaron_examenes in ["sí", "si"]:
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            reprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
            total_alumnos = aprobados + reprobados
            
            if total_alumnos > 0:
                porcentaje = (aprobados / total_alumnos) * 100
                print(f"El porcentaje de alumnos aprobados es: {porcentaje:.2f}%")
            else:
                print("No se evaluaron alumnos.")

    # 2. Práctica Hablada (Jueves)
    elif dia_semana == "jueves":
        asistencia = float(input("Ingrese el porcentaje de asistencia (0-100): "))
        if asistencia > 50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")

    # 3. Inglés para Viajeros (Viernes)
    elif dia_semana == "viernes":
        if (dia_num == 1 and mes_num == 1) or (dia_num == 1 and mes_num == 7):
            print("Comienzo de nuevo ciclo")
            cant_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
            
            ingreso_total = cant_alumnos * arancel
            
            # Formateo dinámico para mostrar entero si no tiene decimales
            if ingreso_total.is_integer():
                ingreso_total = int(ingreso_total)
                
            print(f"El ingreso total es: ${ingreso_total}")