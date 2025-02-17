# producto.py
class Producto:
    """Clase que representa un producto en el inventario."""

    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """Constructor de la clase Producto."""
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precio(self) -> float:
        return self._precio

    # Setters
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")

    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            raise ValueError("El precio no puede ser negativo")

    def __str__(self) -> str:
        """Representación en string del producto."""
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


# inventario.py
class Inventario:
    """Clase que gestiona el inventario de productos."""

    def __init__(self):
        """Constructor de la clase Inventario."""
        self._productos = {}  # Diccionario con ID como clave y Producto como valor

    def agregar_producto(self, nombre: str, cantidad: int, precio: float) -> bool:
        """Agrega un nuevo producto al inventario."""
        # Genera un nuevo ID único
        nuevo_id = max(self._productos.keys(), default=0) + 1

        try:
            producto = Producto(nuevo_id, nombre, cantidad, precio)
            self._productos[nuevo_id] = producto
            return True
        except ValueError as e:
            print(f"Error al agregar producto: {e}")
            return False

    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto del inventario por su ID."""
        if id_producto in self._productos:
            del self._productos[id_producto]
            return True
        return False

    def actualizar_producto(self, id_producto: int, nueva_cantidad: int = None, nuevo_precio: float = None) -> bool:
        """Actualiza la cantidad o precio de un producto."""
        if id_producto not in self._productos:
            return False

        producto = self._productos[id_producto]
        try:
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            return True
        except ValueError as e:
            print(f"Error al actualizar producto: {e}")
            return False

    def buscar_productos(self, nombre: str) -> list:
        """Busca productos por nombre (búsqueda parcial)."""
        return [prod for prod in self._productos.values()
                if nombre.lower() in prod.nombre.lower()]

    def mostrar_productos(self) -> list:
        """Retorna lista de todos los productos."""
        return list(self._productos.values())


# main.py
def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar productos")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    return input("Seleccione una opción: ")


def main():
    inventario = Inventario()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
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

        elif opcion == "2":
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                if inventario.eliminar_producto(id_producto):
                    print("Producto eliminado exitosamente")
                else:
                    print("Producto no encontrado")
            except ValueError:
                print("Error: ID inválido")

        elif opcion == "3":
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                opcion_actualizar = input("¿Qué desea actualizar? (cantidad/precio): ").lower()

                if opcion_actualizar == "cantidad":
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    if inventario.actualizar_producto(id_producto, nueva_cantidad=nueva_cantidad):
                        print("Cantidad actualizada exitosamente")
                    else:
                        print("Error al actualizar la cantidad")

                elif opcion_actualizar == "precio":
                    nuevo_precio = float(input("Nuevo precio: "))
                    if inventario.actualizar_producto(id_producto, nuevo_precio=nuevo_precio):
                        print("Precio actualizado exitosamente")
                    else:
                        print("Error al actualizar el precio")
                else:
                    print("Opción inválida")
            except ValueError:
                print("Error: Valores ingresados no válidos")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            productos = inventario.buscar_productos(nombre)
            if productos:
                print("\nProductos encontrados:")
                for producto in productos:
                    print(producto)
            else:
                print("No se encontraron productos")

        elif opcion == "5":
            productos = inventario.mostrar_productos()
            if productos:
                print("\nLista de productos:")
                for producto in productos:
                    print(producto)
            else:
                print("No hay productos en el inventario")

        elif opcion == "6":
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()