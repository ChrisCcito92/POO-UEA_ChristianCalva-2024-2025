import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("600x450")

        self.tasks = []

        # Contenedor principal
        frame_main = tk.Frame(root)
        frame_main.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Contenedor de entrada de datos
        frame_inputs = tk.Frame(frame_main)
        frame_inputs.pack(pady=5)

        # Etiquetas para los campos de entrada
        tk.Label(frame_inputs, text="Fecha").grid(row=0, column=0, padx=5)
        tk.Label(frame_inputs, text="Hora").grid(row=0, column=1, padx=5)
        tk.Label(frame_inputs, text="Descripción").grid(row=0, column=2, padx=5)

        # Campos de entrada
        self.date_entry = DateEntry(frame_inputs, width=12)
        self.date_entry.grid(row=1, column=0, padx=5)

        self.time_entry = tk.Entry(frame_inputs, width=10)
        self.time_entry.grid(row=1, column=1, padx=5)

        self.desc_entry = tk.Entry(frame_inputs, width=30)
        self.desc_entry.grid(row=1, column=2, padx=5)
        self.desc_entry.bind("<Return>", self.add_task_event)  # Permite añadir tareas con Enter

        # Contenedor de botones
        frame_buttons = tk.Frame(frame_main)
        frame_buttons.pack(pady=5)

        # Botones para manejar las tareas
        self.add_button = tk.Button(frame_buttons, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.edit_button = tk.Button(frame_buttons, text="Editar Tarea", command=self.edit_task)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(frame_buttons, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Contenedor de la lista de tareas con encabezados
        self.task_tree = ttk.Treeview(frame_main, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.task_tree.heading("Fecha", text="Fecha")
        self.task_tree.heading("Hora", text="Hora")
        self.task_tree.heading("Descripción", text="Descripción")
        self.task_tree.pack(pady=10, fill=tk.BOTH, expand=True)
        self.task_tree.bind("<Double-Button-1>", self.toggle_task_completion)  # Doble clic para marcar/desmarcar tarea

        # Etiqueta de ayuda sobre el doble clic
        self.info_label = tk.Label(root, text="Doble clic en una tarea para marcarla o desmarcarla.", fg="gray")
        self.info_label.pack(pady=5)

        # Botón para salir de la aplicación
        self.exit_button = tk.Button(root, text="Salir", command=root.quit)
        self.exit_button.pack(pady=5)

    def add_task(self):
        """Añade una nueva tarea a la lista"""
        date = self.date_entry.get()
        time = self.time_entry.get().strip()
        desc = self.desc_entry.get().strip()

        if date and time and desc:
            self.task_tree.insert("", tk.END, values=(date, time, desc))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def add_task_event(self, event):
        """Permite añadir una tarea al presionar Enter"""
        self.add_task()

    def edit_task(self):
        """Edita la tarea seleccionada"""
        selected_item = self.task_tree.selection()
        if selected_item:
            item_values = self.task_tree.item(selected_item, "values")
            self.date_entry.set_date(item_values[0])
            self.time_entry.delete(0, tk.END)
            self.time_entry.insert(0, item_values[1])
            self.desc_entry.delete(0, tk.END)
            self.desc_entry.insert(0, item_values[2])
            self.task_tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para editar.")

    def delete_task(self):
        """Elimina la tarea seleccionada"""
        selected_item = self.task_tree.selection()
        if selected_item:
            self.task_tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

    def toggle_task_completion(self, event):
        """Marca o desmarca una tarea como completada al hacer doble clic"""
        selected_item = self.task_tree.selection()
        if selected_item:
            item_values = self.task_tree.item(selected_item, "values")
            new_desc = "✔ " + item_values[2] if not item_values[2].startswith("✔ ") else item_values[2][2:]
            self.task_tree.item(selected_item, values=(item_values[0], item_values[1], new_desc))
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()