class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla inmutable con título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {[libro.info[0] for libro in self.libros_prestados]}"

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no disponible para préstamo.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene prestado este libro.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, filtro, valor):
        resultados = [libro for libro in self.libros_disponibles.values() if getattr(libro, filtro, None) == valor]
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Ejemplo de uso
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("1984", "George Orwell", "Ficción", "12345")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "67890")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuario
usuario1 = Usuario("Carlos Pérez", "U001")
biblioteca.registrar_usuario(usuario1)

# Prestar y devolver libros
biblioteca.prestar_libro("U001", "12345")
biblioteca.listar_libros_prestados("U001")
biblioteca.devolver_libro("U001", "12345")
biblioteca.listar_libros_prestados("U001")

# Buscar libros
biblioteca.buscar_libro("categoria", "Ficción")