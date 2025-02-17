# producto
class Producto:

    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.
        Inicializa un producto con su ID, nombre, cantidad en stock y precio unitario.
        """
        self._id = id_producto  # ID único del producto
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad  # Cantidad disponible en inventario
        self._precio = precio  # Precio unitario del producto

    # Métodos Getters (propiedades de solo lectura)
    @property
    def id(self) -> int:
        """
        Devuelve el ID del producto.
        @property permite acceder al atributo como si fuera una propiedad (sin usar paréntesis).
        """
        return self._id

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del producto."""
        return self._nombre

    @property
    def cantidad(self) -> int:
        """Devuelve la cantidad disponible del producto."""
        return self._cantidad

    @property
    def precio(self) -> float:
        """Devuelve el precio unitario del producto."""
        return self._precio

    # Métodos Setters (modifican atributos con validación)
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        """
        Permite modificar la cantidad de un producto.
        Se asegura de que la cantidad no sea negativa.
        """
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")  # Lanza un error si el valor es inválido

    @precio.setter
    def precio(self, nuevo_precio: float):
        """
        Permite modificar el precio del producto.
        Se asegura de que el precio no sea negativo.
        """
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")  # Lanza un error si el valor es inválido

    def __str__(self) -> str:
        """
        Representación en cadena del objeto Producto.
        Retorna una cadena con la información del producto.
        """
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


# inventario
class Inventario:
    """Clase que gestiona el inventario de productos."""

    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa un diccionario vacío para almacenar productos.
        La clave es el ID del producto y el valor es una instancia de Producto.
        """
        self._productos = {}  # Diccionario de productos

    def agregar_producto(self, nombre: str, cantidad: int, precio: float) -> bool:
        """
        Agrega un nuevo producto al inventario asignándole un ID único.
        Retorna True si se agregó correctamente, False en caso de error.
        """
        # Genera un nuevo ID basado en el ID más alto actual
        nuevo_id = max(self._productos.keys(), default=0) + 1

        try:
            producto = Producto(nuevo_id, nombre, cantidad, precio)  # Crea un nuevo producto
            self._productos[nuevo_id] = producto  # Lo agrega al inventario
            return True
        except ValueError as e:
            print(f"Error al agregar producto: {e}")  # Manejo de errores si hay valores inválidos
            return False

    def eliminar_producto(self, id_producto: int) -> bool:
        """
        Elimina un producto del inventario por su ID.
        Retorna True si se eliminó correctamente, False si el producto no existe.
        """
        if id_producto in self._productos:
            del self._productos[id_producto]  # Elimina el producto del diccionario
            return True
        return False

    def actualizar_producto(self, id_producto: int, nueva_cantidad: int = None, nuevo_precio: float = None) -> bool:
        """
        Actualiza la cantidad o precio de un producto en el inventario.
        Retorna True si la actualización es exitosa, False si el producto no existe.
        """
        if id_producto not in self._productos:
            return False  # Retorna False si el producto no está en el inventario

        producto = self._productos[id_producto]  # Obtiene el producto

        try:
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad  # Usa el setter para validar y actualizar
            if nuevo_precio is not None:
                producto.precio = nuevo_precio  # Usa el setter para validar y actualizar
            return True
        except ValueError as e:
            print(f"Error al actualizar producto: {e}")  # Muestra un error si el nuevo valor no es válido
            return False

    def buscar_productos(self, nombre: str) -> list:
        """
        Busca productos cuyo nombre contenga la palabra clave (búsqueda parcial).
        Retorna una lista de productos encontrados.
        """
        return [prod for prod in self._productos.values()
                if nombre.lower() in prod.nombre.lower()]  # Comparación sin distinguir mayúsculas y minúsculas

    def mostrar_productos(self) -> list:
        """
        Retorna una lista con todos los productos del inventario.
        """
        return list(self._productos.values())  # Retorna todos los productos en forma de lista


# main.py
def mostrar_menu():
    """Muestra el menú principal de opciones y retorna la selección del usuario."""
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar productos")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    return input("Seleccione una opción: ")  # Devuelve la opción elegida por el usuario


def main():
    """Función principal que ejecuta el programa."""
    inventario = Inventario()  # Crea una instancia del inventario

    while True:
        opcion = mostrar_menu()  # Muestra el menú y obtiene la opción del usuario

        if opcion == "1":  # Agregar producto
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                if inventario.agregar_producto(nombre, cantidad, precio):
                    print("Producto agregado exitosamente")
                else:
                    print("Error al agregar el producto")
            except ValueError:
                print("Error: Los valores ingresados no son válidos")

        elif opcion == "2":  # Eliminar producto
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                if inventario.eliminar_producto(id_producto):
                    print("Producto eliminado exitosamente")
                else:
                    print("Producto no encontrado")
            except ValueError:
                print("Error: ID inválido")

        elif opcion == "3":  # Actualizar producto
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                opcion_actualizar = input("¿Qué desea actualizar? (cantidad/precio): ").lower()

                if opcion_actualizar == "cantidad":
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    if inventario.actualizar_producto(id_producto, nueva_cantidad=nueva_cantidad):
                        print("Cantidad actualizada exitosamente")
                elif opcion_actualizar == "precio":
                    nuevo_precio = float(input("Nuevo precio: "))
                    if inventario.actualizar_producto(id_producto, nuevo_precio=nuevo_precio):
                        print("Precio actualizado exitosamente")
                else:
                    print("Opción inválida")
            except ValueError:
                print("Error: Valores ingresados no válidos")

        elif opcion == "4":  # Buscar productos
            nombre = input("Nombre a del producto: ")
            productos = inventario.buscar_productos(nombre)
            print("\n".join(map(str, productos)) if productos else "No se encontraron productos")

        elif opcion == "5":  # Mostrar todos los productos
            productos = inventario.mostrar_productos()
            print("\n".join(map(str, productos)) if productos else "No hay productos en el inventario")

        elif opcion == "6":  # Salir
            print("¡Gracias por usar el sistema de inventario!")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()  # Ejecuta el programa