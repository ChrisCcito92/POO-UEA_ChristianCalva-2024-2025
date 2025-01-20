# Clase padre: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self._modelo = modelo  # Atributo encapsulado

    # Metodo para mover el carro
    def mover(self):
        print("El vehículo se está moviendo")

    # Metodo para obtener el atributo encapsulado
    def obtener_modelo(self):
        return self._modelo

    # Metodo para establecer el atributo encapsulado
    def establecer_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

# Clase hija: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, tipo_combustible):
        # Llamada al constructor de la clase padre
        super().__init__(marca, modelo)
        self.tipo_combustible = tipo_combustible  # Atributo específico del coche

    # Sobrescritura del metodo mover
    def mover(self):
        print(f"El coche {self.marca} {self._modelo} está avanzando por la carretera")

    # Metodo especifico para el coche
    def informacion_combustible(self):
        print(f"Este coche usa {self.tipo_combustible} como combustible.")


# Creación de las instancias
vehiculo_generico = Vehiculo("Vehículo Genérico", "Modelo Ionic")
coche1 = Coche("Kia", "Picanto", "Gasolina")

# Demostracion de Polimorfismo: el mismo metodo 'mover' se comporta de manera diferente
vehiculo_generico.mover()  # Llamada al metodo de la clase padre
coche1.mover()  # Llamada al metodo sobrescrito en la clase derivada

# Uso de metodos obetener y establecer para la encapsulacion
print(f"Modelo del vehículo genérico: {vehiculo_generico.obtener_modelo()}")
vehiculo_generico.establecer_modelo("Nuevo Modelo Z")
print(f"Nuevo modelo del vehículo genérico: {vehiculo_generico.obtener_modelo()}")

# Informacion especifica del coche
coche1.informacion_combustible()