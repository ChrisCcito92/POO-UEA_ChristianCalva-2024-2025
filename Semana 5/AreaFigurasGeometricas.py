# Este programa calcula el área de diferentes figuras geométricas según la entrada del usuario.
# El usuario podrá elegir la figura de un menú y proporcionar los datos solicitados.

import math  # Importa la librería math para operaciones matemáticas

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    # Calcula el área de un círculo dado su radio.
    area = math.pi * radio ** 2 # El área se calcula con la fórmula A = pi * radio^2.
    return area


# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    # Calcula el área de un cuadrado dado el lado.
    area = lado ** 2 # El área se calcula con la fórmula A = lado^2.
    return area


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    # Calcula el área de un triángulo dado su base y altura.
    area = (base * altura) / 2 # El área se calcula con la fórmula A = (base * altura) / 2.
    return area


# Función principal con el menú de opciones
def main():
    while True:
        # Menú de opciones
        print("\nSeleccione el número de la figura para calcular el área:")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Triángulo")
        print("4. Salir")

        # Obtiene la opción del usuario
        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            # Calcula el área de un círculo
            radio = float(input("Ingrese el radio del círculo: "))
            area_circulo = calcular_area_circulo(radio)
            print(f"El área del círculo con radio {radio} cm es {area_circulo:.2f} cm cuadrados.")

        elif opcion == '2':
            # Calcula el área de un cuadrado
            lado = float(input("Ingrese el lado del cuadrado: "))
            area_cuadrado = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado con lado {lado} cm es {area_cuadrado:.2f} cm cuadrados.")

        elif opcion == '3':
            # Calcula el  área de un triángulo
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area_triangulo = calcular_area_triangulo(base, altura)
            print(
                f"El área del triángulo con base {base} cm y altura {altura} cm es {area_triangulo:.2f} cm cuadrados.")

        elif opcion == '4':
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


# Llama a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
