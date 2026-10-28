#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicios propuestos en clase

# ==============================================================================
# EJERCICIOS PROPUESTOS EN CLASE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Factorial de un número
# ------------------------------------------------------------------------------
def factorial(n):
    """Calcula el producto de todos los enteros desde 1 hasta n."""
    # Caso base: si llegamos a 0 o 1, la función se detiene y devuelve 1
    if n <= 1:
        return 1
    # Paso recursivo: n multiplicado por el factorial del número anterior
    return n * factorial(n - 1)


# ------------------------------------------------------------------------------
# 2. Filtrar números pares y elevarlos al cuadrado
# ------------------------------------------------------------------------------
def filtrar_y_cuadrado(lista):
    """Filtra pares y los eleva al cuadrado en un solo paso recursivo."""
    # Caso base: si la lista está vacía, devolvemos una lista vacía
    if not lista:
        return []
    
    primer_elemento = lista[0]
    resto = lista[1:]
    
    # Si es par, lo elevamos al cuadrado y lo unimos al resultado del resto
    if primer_elemento % 2 == 0:
        return [primer_elemento ** 2] + filtrar_y_cuadrado(resto)
    else:
        # Si no es par, lo ignoramos y continuamos con el resto
        return filtrar_y_cuadrado(resto)


# ------------------------------------------------------------------------------
# 3. Suma total de una lista
# ------------------------------------------------------------------------------
def suma_recursiva(lista):
    """Devuelve la suma total de los elementos de una lista."""
    # Caso base: si la lista no tiene elementos, la suma es 0
    if not lista:
        return 0
    # Paso recursivo: primer elemento + suma del resto de la lista
    return lista[0] + suma_recursiva(lista[1:])


# ------------------------------------------------------------------------------
# 4. Invertir una cadena de texto
# ------------------------------------------------------------------------------
def invertir_cadena(texto):
    """Devuelve un string invertido recursivamente."""
    # Caso base: si la cadena tiene 0 o 1 carácter, ya está invertida
    if len(texto) <= 1:
        return texto
    # Paso recursivo: última letra + inversión del resto del texto
    return texto[-1] + invertir_cadena(texto[:-1])


# ------------------------------------------------------------------------------
# 5. Encontrar el número máximo de una lista
# ------------------------------------------------------------------------------
def maximo_recursivo(lista):
    """Encuentra el número más grande comparando elementos uno a uno."""
    # Caso base: si solo queda un número, ese es el máximo de esa sublista
    if len(lista) == 1:
        return lista[0]
    
    # Obtenemos el máximo del resto de la lista
    max_del_resto = maximo_recursivo(lista[1:])
    
    # Comparamos el primer elemento con el máximo del resto
    if lista[0] > max_del_resto:
        return lista[0]
    else:
        return max_del_resto


# ==============================================================================
# PRUEBAS / EJECUCIÓN DEL CÓDIGO
# ==============================================================================
if __name__ == "__main__":
    print("--- DEMOSTRACIÓN DE EJERCICIOS ---")
    
    # 1. Factorial
    num_fact = 3
    print(f"1. Factorial de {num_fact}: {factorial(num_fact)}")
    
    # 2. Filtrar y elevar al cuadrado
    lista_cuadrados = [1, 2, 3, 4, 5, 6]
    print(f"2. Pares al cuadrado de {lista_cuadrados}: {filtrar_y_cuadrado(lista_cuadrados)}")
    
    # 3. Suma recursiva
    lista_suma = [5, 10, 15]
    print(f"3. Suma de {lista_suma}: {suma_recursiva(lista_suma)}")
    
    # 4. Invertir cadena
    cadena = "Programacion"
    print(f"4. Cadena '{cadena}' invertida: {invertir_cadena(cadena)}")
    
    # 5. Máximo recursivo
    lista_max = [3, 17, 8, 25, 4]
    print(f"5. El número máximo en {lista_max} es: {maximo_recursivo(lista_max)}")