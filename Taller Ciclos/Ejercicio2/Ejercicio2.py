#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica


#Ejercicio 2


'''Escriba un programa para que la siguiente lista [2,4,3,1,6,7,5,8,9,10] se ordene de
menor a mayor (orden ascendente). Implementar con ciclos y posteriormente usar una función
predeterminada de Python para verificar el funcionamiento del mismo.
'''
#IMPLEMENTACIÓN CON CICLO FOR

# Lista  dada por el ejercicio
ListaNumero1_for = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]
ListaNumero2 = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]
print("Lista original:", ListaNumero1_for)

# 1. ORDENAMIENTO CON CICLOS (Algoritmo de Burbuja)

# Hacemos una copia para no modificar la lista original directamente
ListaCopia = list(ListaNumero1_for)
#Se cuenta la cantidad de elementos de la 'ListaCopia'
NumeroElementos = len(ListaCopia)

# Ciclo externo: recorre la lista varias veces
for i in range(NumeroElementos):
    # Ciclo interno: compara elementos adyacentes
    for j in range(0, NumeroElementos - i - 1):
        if ListaCopia[j] > ListaCopia[j + 1]:
            # Intercambio de posiciones si el elemento actual es mayor que el siguiente
            temp = ListaCopia[j]
            ListaCopia[j] = ListaCopia[j + 1]
            ListaCopia[j + 1] = temp

print("\n1. Lista ordenada con ciclos (método burbuja):")
print(ListaCopia)




# 2. VERIFICACIÓN CON FUNCIÓN PREDETERMINADA DE PYTHON
lista_verificacion = list(ListaNumero2 )
lista_verificacion.sort()  # Método predeterminado de Python para ordenar

print("\n2. Lista ordenada con la función predeterminada .sort():")
print(lista_verificacion)

# Comprobación de que ambos métodos dan el mismo resultado
if ListaCopia == lista_verificacion:
    print("¡El ordenamiento mediante ciclos funciona correctamente!")
else:
    print("Hay un error en la lógica del ordenamiento.")



