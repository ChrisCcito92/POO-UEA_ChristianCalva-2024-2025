# Directorio de contactos
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def mostrar_informacion(self):
        # Metodo para mostrar la información del contacto
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")


# Clase para gestionar la lista de contactos
class GestionContactos:
    def __init__(self):
        self.contactos = [] # Inicia la lista vacía

    def agregar_contacto(self, contacto):
        # Metodo para agregar un contacto a la lista de contactos
        self.contactos.append(contacto)
        print(f"Contacto '{contacto.nombre}' agregado exitosamente.\n")

    def buscar_contacto(self, nombre):
        # Metodo para buscar un contacto por su nombre
        # Devuelve un mensaje con el contacto encontrado o si no existe
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():  # Comparacion
                return contacto
        return None

    def mostrar_todos(self):
        # Metodo para mostrar todos los contactos en la lista
        if not self.contactos:
            print("No hay contactos en la lista.\n")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                contacto.mostrar_informacion()
                print("-" * 20)  # Separador visual entre contactos


# Ejemplos
gestion = GestionContactos()  # Crea instancia para gestionar contactos

# Crea algunos contactos de ejmplo
contacto1 = Contacto("Juan Pérez", "0987456321", "juanpe@gmail.com")
contacto2 = Contacto("María López", "0987654321", "marialo@hotmail.com")

# Agrega los contactos a la lista
gestion.agregar_contacto(contacto1)
gestion.agregar_contacto(contacto2)

# Muestra todos los contactos
gestion.mostrar_todos()

# Busca un contacto por nombre
nombre_buscar = "Juan Pérez"
contacto_encontrado = gestion.buscar_contacto(nombre_buscar)

if contacto_encontrado:
    print(f"\nContacto encontrado:")
    contacto_encontrado.mostrar_informacion()
else:
    print(f"\nNo se encontró un contacto con el nombre '{nombre_buscar}'.")