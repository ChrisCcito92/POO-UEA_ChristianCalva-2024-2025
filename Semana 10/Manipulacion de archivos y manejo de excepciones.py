class Producto:
    # Constructor de la clase Producto que recibe id, nombre, cantidad y precio.
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self._id = id_producto  # Asigna el id del producto a la variable de instancia _id
        self._nombre = nombre  # Asigna el nombre del producto a la variable de instancia _nombre
        self._cantidad = cantidad  # Asigna la cantidad del producto a la variable de instancia _cantidad
        self._precio = precio  # Asigna el precio del producto a la variable de instancia _precio

    # Propiedad para obtener el ID del producto
    @property
    def id(self) -> int:
        return self._id  # Devuelve el valor de _id

    # Propiedad para obtener el nombre del producto
    @property
    def nombre(self) -> str:
        return self._nombre  # Devuelve el valor de _nombre

    # Propiedad para obtener la cantidad del producto
    @property
    def cantidad(self) -> int:
        return self._cantidad  # Devuelve el valor de _cantidad

    # Propiedad para obtener el precio del producto
    @property
    def precio(self) -> float:
        return self._precio  # Devuelve el valor de _precio

    # Setter para la cantidad (valida que no sea negativa)
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        if nueva_cantidad >= 0:  # Verifica que la nueva cantidad no sea negativa
            self._cantidad = nueva_cantidad  # Si es válida, asigna el nuevo valor a _cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")  # Si es negativa, lanza un error

    # Setter para el precio (valida que no sea negativo)
    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio >= 0:  # Verifica que el nuevo precio no sea negativo
            self._precio = nuevo_precio  # Si es válido, asigna el nuevo valor a _precio
        else:
            raise ValueError("El precio no puede ser negativo")  # Si es negativo, lanza un error

    # Metodo que devuelve una cadena con la información del producto
    def __str__(self) -> str:
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"  # Retorna una representación legible del producto

class Inventario:
    """Clase que gestiona el inventario de productos."""

    # Constructor de la clase Inventario, que inicializa el diccionario de productos
    def __init__(self, archivo: str = "inventario.txt"):
        self._productos = {}  # Diccionario vacío donde se almacenarán los productos
        self.archivo = archivo  # Archivo donde se guardará el inventario
        self.cargar_inventario()  # Llama a la función cargar_inventario para cargar los datos del archivo

    # Función que carga los productos desde un archivo
    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as file:  # Intenta abrir el archivo en modo lectura
                for linea in file:  # Recorre cada línea del archivo
                    partes = linea.strip().split(",")  # Divide la línea en partes usando la coma como separador
                    if len(partes) == 4:  # Si la línea tiene el formato correcto (4 elementos)
                        id_producto = int(partes[0])  # Convierte el ID a entero
                        nombre = partes[1]  # El nombre es el segundo elemento
                        cantidad = int(partes[2])  # La cantidad es el tercer elemento
                        precio = float(partes[3])  # El precio es el cuarto elemento
                        producto = Producto(id_producto, nombre, cantidad, precio)  # Crea una instancia de Producto
                        self._productos[id_producto] = producto  # Agrega el producto al diccionario usando su ID como clave
        except FileNotFoundError:
            print(f"El archivo {self.archivo} no existe. Se creará un nuevo archivo.")  # Maneja si el archivo no existe
        except PermissionError:
            print(f"No se tienen permisos para acceder al archivo {self.archivo}.")  # Maneja si no se tiene acceso al archivo
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")  # Maneja cualquier otro error

    # Función que guarda los productos en un archivo
    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as file:  # Abre el archivo en modo escritura
                for producto in self._productos.values():  # Recorre todos los productos en el inventario
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")  # Escribe los datos de cada producto en el archivo
        except PermissionError:
            print(f"No se tienen permisos para escribir en el archivo {self.archivo}.")  # Maneja si no se tiene acceso para escribir
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")  # Maneja cualquier otro error

    # Función que agrega un producto al inventario
    def agregar_producto(self, nombre: str, cantidad: int, precio: float) -> bool:
        nuevo_id = max(self._productos.keys(), default=0) + 1  # Genera un nuevo ID único basado en el máximo ID actual
        try:
            producto = Producto(nuevo_id, nombre, cantidad, precio)  # Crea un nuevo producto con los datos proporcionados
            self._productos[nuevo_id] = producto  # Agrega el producto al diccionario
            self.guardar_inventario()  # Guarda el inventario actualizado en el archivo
            return True  # Retorna True si el producto fue agregado exitosamente
        except ValueError as e:
            print(f"Error al agregar producto: {e}")  # Maneja cualquier error en la creación del producto
            return False  # Retorna False si hubo un error

    # Función que elimina un producto por su ID
    def eliminar_producto(self, id_producto: int) -> bool:
        if id_producto in self._productos:  # Verifica si el producto existe en el inventario
            del self._productos[id_producto]  # Elimina el producto del diccionario
            self.guardar_inventario()  # Guarda el inventario actualizado
            return True  # Retorna True si el producto fue eliminado correctamente
        return False  # Retorna False si el producto no fue encontrado

    # Función que actualiza la cantidad o el precio de un producto
    def actualizar_producto(self, id_producto: int, nueva_cantidad: int = None, nuevo_precio: float = None) -> bool:
        if id_producto not in self._productos:  # Verifica si el producto existe en el inventario
            return False  # Si no existe, retorna False

        producto = self._productos[id_producto]  # Obtiene la instancia del producto
        try:
            if nueva_cantidad is not None:  # Si se pasa una nueva cantidad, la actualiza
                producto.cantidad = nueva_cantidad
            if nuevo_precio is not None:  # Si se pasa un nuevo precio, lo actualiza
                producto.precio = nuevo_precio
            self.guardar_inventario()  # Guarda el inventario actualizado
            return True  # Retorna True si la actualización fue exitosa
        except ValueError as e:
            print(f"Error al actualizar producto: {e}")  # Maneja errores al intentar actualizar
            return False  # Retorna False si hubo un error

    # Función que busca productos por nombre
    def buscar_productos(self, nombre: str) -> list:
        return [prod for prod in self._productos.values() if nombre.lower() in prod.nombre.lower()]  # Filtra los productos cuyo nombre contenga la palabra clave

    # Función que devuelve todos los productos del inventario
    def mostrar_productos(self) -> list:
        return list(self._productos.values())  # Devuelve todos los productos como una lista

def mostrar_menu():
    """Muestra el menú de opciones y devuelve la opción seleccionada por el usuario."""
    print("\n--- Menú de Inventario ---")  # Muestra el título del menú
    print("1. Agregar producto")  # Opción para agregar un producto
    print("2. Eliminar producto")  # Opción para eliminar un producto
    print("3. Actualizar producto")  # Opción para actualizar un producto
    print("4. Buscar productos")  # Opción para buscar productos por nombre
    print("5. Mostrar todos los productos")  # Opción para mostrar todos los productos
    print("6. Salir")  # Opción para salir del programa
    opcion = input("Seleccione una opción: ")  # Solicita al usuario que seleccione una opción
    return opcion  # Retorna la opción seleccionada

def main():
    """Función principal que ejecuta el programa."""
    inventario = Inventario()  # Crea una instancia de la clase Inventario

    while True:  # Bucle infinito para que el programa siga ejecutándose
        opcion = mostrar_menu()  # Muestra el menú y obtiene la opción seleccionada por el usuario

        if opcion == "1":  # Agregar producto
            nombre = input("Nombre del producto: ")  # Solicita el nombre del producto
            try:
                cantidad = int(input("Cantidad: "))  # Solicita la cantidad y la convierte a entero
                precio = float(input("Precio: "))  # Solicita el precio y lo convierte a flotante
                if inventario.agregar_producto(nombre, cantidad, precio):  # Agrega el producto
                    print("Producto agregado exitosamente")  # Mensaje de éxito
                else:
                    print("Error al agregar el producto")  # Mensaje de error
            except ValueError:  # Si hay un error de conversión de tipo de datos
                print("Error: Los valores ingresados no son válidos")  # Mensaje de error

        elif opcion == "2":  # Eliminar producto
            try:
                id_producto = int(input("ID del producto a eliminar: "))  # Solicita el ID del producto a eliminar
                if inventario.eliminar_producto(id_producto):  # Intenta eliminar el producto
                    print("Producto eliminado exitosamente")  # Mensaje de éxito
                else:
                    print("Producto no encontrado")  # Mensaje si no se encuentra el producto
            except ValueError:  # Maneja cualquier error de conversión
                print("Error: El ID ingresado no es válido")  # Mensaje de error

        elif opcion == "3":  # Actualizar producto
            try:
                id_producto = int(input("ID del producto a actualizar: "))  # Solicita el ID del producto
                nueva_cantidad = int(input("Nueva cantidad (deje en blanco si no cambia): ") or 0)  # Solicita la nueva cantidad
                nuevo_precio = float(input("Nuevo precio (deje en blanco si no cambia): ") or 0)  # Solicita el nuevo precio
                if inventario.actualizar_producto(id_producto, nueva_cantidad or None, nuevo_precio or None):  # Intenta actualizar
                    print("Producto actualizado exitosamente")  # Mensaje de éxito
                else:
                    print("Producto no encontrado")  # Mensaje si no se encuentra el producto
            except ValueError:  # Si hay un error de conversión de datos
                print("Error: Los valores ingresados no son válidos")  # Mensaje de error

        elif opcion == "4":  # Buscar productos
            nombre = input("Ingrese el nombre del producto a buscar: ")  # Solicita el nombre del producto
            resultados = inventario.buscar_productos(nombre)  # Busca productos por nombre
            if resultados:
                for prod in resultados:
                    print(prod)  # Muestra cada producto encontrado
            else:
                print("No se encontraron productos")  # Mensaje si no hay productos encontrados

        elif opcion == "5":  # Mostrar todos los productos
            productos = inventario.mostrar_productos()  # Obtiene todos los productos
            for prod in productos:
                print(prod)  # Muestra cada producto

        elif opcion == "6":  # Salir del programa
            print("Saliendo del programa...")
            print("Regrese pronto!")
            break  # Sale del bucle y termina el programa

        else:
            print("Opción no válida, intente de nuevo")  # Si la opción no es válida

# Ejecutar la función principal
if __name__ == "__main__":
    main()