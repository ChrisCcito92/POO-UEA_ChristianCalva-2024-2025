def calcular_temperatura():
    print("*** Cálculo del promedio semanal del clima ***")
    dias_sem = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = {}  # Diccionario para almacenar las temperaturas por día
    for dia in dias_sem:
        # Solicita la temperatura para cada día y almacena en el diccionario
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas[dia] = temp
    # Calcula el promedio de las temperaturas
    promedio = sum(temperaturas.values()) / len(temperaturas)
    # Imprime el promedio con dos decimales
    print(f"El promedio semanal de temperatura es: {promedio:.2f} grados")
# Llama a la función para ejecutar el cálculo
calcular_temperatura()