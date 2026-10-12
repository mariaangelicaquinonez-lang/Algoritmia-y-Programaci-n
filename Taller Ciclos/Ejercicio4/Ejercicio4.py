#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 4
'''
Usted tiene acceso a la base de datos de “student_scores” en un formato de diccio-
nario donde las llaves son los nombres de los estudiantes y los valores son las notas de ellos.

Al finalizar el programa, se debe tener un diccionario denominado “student_grades”, que con-
tiene los nombres de los estudiantes como llaves y los siguientes mensajes como valores:

Scores 91 - 100: Grade = “Outstanding”
Scores 81 - 90: Grade = “Exceeds Expectations”
Scores 71 - 80: Grade = “Acceptable”
Scores 70 or lower: Grade = “Fail”

Harry 88
Ron 78
Hermione 95
Draco 75
Neville 60

'''

# Diccionario inicial con las notas de los estudiantes (Hermione = 95)
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

# Diccionario vacío donde se almacenarán las calificaciones finales
student_grades = {}

# Recorremos el diccionario usando un ciclo for e .items()
for key_student, score_valores in student_scores.items():
    # Evaluación de rangos según la tabla del taller
    if score_valores >= 91 and score_valores <= 100:
        grade = "Outstanding"
    elif score_valores >= 81 and score_valores <= 90:
        grade = "Exceeds Expectations"
    elif score_valores >= 71 and score_valores <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    # Asignamos la calificación al nuevo diccionario
    student_grades[key_student] = grade

# Mostrar el diccionario resultante
print("--- Diccionario de Calificaciones (student_grades) ---")
print(student_grades)

# Impresión formateada para mejor visualización
print("\n--- Resultado Detallado ---")
for student, grade in student_grades.items():
    print(f"Student: {student} => Grade:{grade}")