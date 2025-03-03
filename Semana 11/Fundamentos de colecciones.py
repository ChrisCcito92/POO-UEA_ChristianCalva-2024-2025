class Producto:
    # Constructor de la clase Producto, define los atributos del producto
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo  # Código único del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.cantidad = cantidad  # Cantidad disponible en el inventario

    # Representación en cadena del producto
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

class Inventario:
    # Constructor de la clase Inventario, inicializa un diccionario vacío de productos
    def __init__(self):
        self.productos = {}  # Se usa un diccionario para mejorar la eficiencia en las búsquedas

    # Metodo para agregar un producto al inventario
    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto  # Se almacena en el diccionario con su código como clave

    # Metodo para eliminar un producto del inventario por su código
    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]  # Se elimina el producto si existe en el inventario
        else:
            print("Producto no encontrado.")

    # Metodo para actualizar el precio y/o cantidad de un producto
    def actualizar_producto(self, codigo, nuevo_precio=None, nueva_cantidad=None):
        if codigo in self.productos:
            producto = self.productos[codigo]  # Se obtiene el producto del diccionario
            if nuevo_precio is not None:
                producto.precio = nuevo_precio  # Actualiza el precio si se proporciona uno nuevo
            if nueva_cantidad is not None:
                producto.cantidad = nueva_cantidad  # Actualiza la cantidad si se proporciona una nueva
        else:
            print("Producto no encontrado.")

    # Metodo para mostrar todos los productos del inventario
    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():  # Se recorren los valores del diccionario
                print(producto)
        else:
            print("No hay productos en el inventario.")

# Función que maneja el menú de opciones para interactuar con el inventario

def menu():
    inventario = Inventario()  # Se crea una instancia del inventario
    while True:
        # Mostrar opciones del menú
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")  # Captura la opción ingresada por el usuario

        if opcion == "1":
            # Opción para agregar un nuevo producto
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))  # Se convierte a float porque es un valor numérico
            cantidad = int(input("Cantidad: "))  # Se convierte a int porque es un valor entero
            inventario.agregar_producto(Producto(codigo, nombre, precio, cantidad))
        elif opcion == "2":
            # Opción para eliminar un producto por su código
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "3":
            # Opción para actualizar un producto existente
            codigo = input("Código del producto a actualizar: ")
            nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(
                codigo,
                float(nuevo_precio) if nuevo_precio else None,  # Convierte a float si se ingresa un valor
                int(nueva_cantidad) if nueva_cantidad else None  # Convierte a int si se ingresa un valor
            )
        elif opcion == "4":
            # Opción para mostrar todos los productos en el inventario
            inventario.mostrar_productos()
        elif opcion == "5":
            # Salir del programa
            break
        else:
            # Mensaje de error si la opción no es válida
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada principal del programa
if __name__ == "__main__":
    menu()