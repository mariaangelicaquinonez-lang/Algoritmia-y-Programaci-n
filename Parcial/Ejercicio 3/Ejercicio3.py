#Nombre: Maria Angelica Quiñonez Valencia
#Codigo: 1006386457
#Ingenieria Electrica
#Ejercicio 3

'''
Diseñe una máquina de arroz para una empresa que debe estar en funcionamiento constante
por largos periodos de tiempo. La máquina debe verificar si hay una bolsa, para después vaciar
el arroz en dicha bolsa, y una vez terminado ese proceso sellarla, para después empacarla en
una caja para su distribución. Nota: para representar la caja se puede hacer uso de alguno
de los métodos de almacenamiento de datos vistos en clase.

a) Identificar las entradas y salidas.
b) Hacer el diagrama de flujo que resuelva el problema.
c) Implementar el código del problema.
d) Demostrar el correcto funcionamiento del código.

'''

# Estructura de almacenamiento (Lista para la caja)
caja = [] 

# Variables de control
estado_maquina = "encendida"
num_bolsa = 1

print("--- MÁQUINA EMPACADORA DE ARROZ EN FUNCIONAMIENTO 🌾 ---")

# Ciclo continuo de la máquina
while estado_maquina == "encendida":
    sensor_bolsa = input("\n ¿Hay una bolsa lista en el dispensador? (si/no): ")
    
    if sensor_bolsa == "si":
        print(">> 1. Vaciando arroz en la bolsa...")
        print(">> 2. Sellando la bolsa herméticamente...")
        
        # Guardar la bolsa en la caja utilizando el método .append()
        etiqueta_bolsa = "Bolsa #" + str(num_bolsa)
        caja.append(etiqueta_bolsa)
        
        print(">> 3. ¡Bolsa empacada con éxito en la caja! ")
        num_bolsa = num_bolsa + 1
    else:
        print("ALERTA: No hay bolsa detectada. La máquina está en espera...")
    
    # Control para mantener la máquina funcionando constantemente
    continuar = input("\n¿Desea mantener la máquina encendida? (si/no): ")
    if continuar != "si":
        estado_maquina = "apagada"

print("\n=========================================")
print("RESUMEN DEL PROCESO")
print("Contenido final de la caja:", caja)
print("Total de bolsas empacadas:", len(caja))
print("=========================================")