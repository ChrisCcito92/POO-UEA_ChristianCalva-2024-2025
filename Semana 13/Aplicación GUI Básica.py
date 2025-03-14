import tkinter as tk
from tkinter import messagebox

# Clase principal que maneja la aplicación GUI
class AplicacionGUI:
    def __init__(self, root):
        # Inicialización de la ventana principal
        self.root = root
        self.root.title("Lista de Tareas")  # Título de la ventana
        self.root.geometry("400x400")  # Tamaño de la ventana
        self.root.configure(bg="#f0f0f0")  # Color de fondo de la ventana

        # Crear una barra de menú
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        # Menú "Archivo" con la opción "Salir"
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Salir", command=self.root.quit)

        # Etiqueta que indica al usuario que ingrese una tarea
        self.label = tk.Label(root, text="Ingrese una tarea:", bg="#f0f0f0", fg="blue")
        self.label.pack(pady=5)

        # Campo de entrada de texto
        self.entry = tk.Entry(root, width=40, bg="#e0e0e0", fg="black")
        self.entry.pack(pady=5)

        # Botones para agregar, actualizar y eliminar tareas
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_tarea, bg="lightgreen", fg="black")
        self.boton_agregar.pack(pady=5)

        self.boton_actualizar = tk.Button(root, text="Actualizar", command=self.actualizar_tarea, bg="lightblue", fg="black")
        self.boton_actualizar.pack(pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_tarea, bg="salmon", fg="black")
        self.boton_eliminar.pack(pady=5)

        # Lista para mostrar las tareas
        self.lista_tareas = tk.Listbox(root, height=15, width=50, bg="#ffffff", fg="black", selectbackground="gray")
        self.lista_tareas.pack(pady=5)

    # Metodo para agregar una tarea a la lista
    def agregar_tarea(self):
        tarea = self.entry.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea antes de agregar.")

    # Metodo para actualizar una tarea seleccionada
    def actualizar_tarea(self):
        try:
            seleccion = self.lista_tareas.curselection()[0]
            nueva_tarea = self.entry.get()
            if nueva_tarea:
                self.lista_tareas.delete(seleccion)
                self.lista_tareas.insert(seleccion, nueva_tarea)
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Advertencia", "Ingrese la tarea actualizada.")
        except IndexError:
            messagebox.showerror("Error", "Seleccione una tarea para actualizar.")

    # Metodo para eliminar una tarea seleccionada
    def eliminar_tarea(self):
        try:
            seleccion = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(seleccion)
        except IndexError:
            messagebox.showerror("Error", "Seleccione una tarea para eliminar.")

# Bloque principal que ejecuta la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = AplicacionGUI(root)  # Instancia de la clase AplicacionGUI
    root.mainloop()  # Inicia el bucle principal de la aplicación