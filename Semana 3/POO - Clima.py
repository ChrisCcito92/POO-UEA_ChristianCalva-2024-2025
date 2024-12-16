# Creamos la clase
class ClimaSemanal:
    # El metodo __init__ se ejecuta al crear una instancia de la clase
    def __init__(self):
        self.temperaturas = {}  # Inicializa un diccionario para almacenar las temperaturas
    def ingresar_temperaturas(self):
        # Lista de días de la semana
        dias_sem = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for dia in dias_sem:
            # Solicita al usuario ingresar la temperatura correspondiente a cada día
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.temperaturas[dia] = temp  # Almacena la temperatura en el diccionario
    def calcular_promedio(self):
        # Verifica si no se han ingresado temperaturas
        if len(self.temperaturas) == 0:
            print("No se han ingresado temperaturas.")
            return 0
        # Calcula el promedio de las temperaturas almacenadas
        return sum(self.temperaturas.values()) / len(self.temperaturas)
# Función principal para ejecutar el programa
def main_temp():
    print("*** Cálculo del promedio semanal del clima ***")
    clima = ClimaSemanal()  # Crea una instancia de la clase ClimaSemanal
    clima.ingresar_temperaturas()  # Solicita al usuario ingresar las temperaturas
    promedio = clima.calcular_promedio()  # Calcula el promedio de las temperaturas
    print(f"El promedio semanal de temperatura es: {promedio:.2f} grados")  # Imprime el promedio con dos decimales
# Llama a la función principal
main_temp()