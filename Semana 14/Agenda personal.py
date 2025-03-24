import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import csv
import os

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("625x430")

        self.filename = "agenda.csv"

        # Crear el contenedor principal
        frame_main = tk.Frame(root)
        frame_main.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Contenedor izquierdo para el calendario
        frame_left = tk.Frame(frame_main)
        frame_left.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        tk.Label(frame_left, text="Fecha:").pack()
        self.date_entry = DateEntry(frame_left, width=12, background='black', foreground='white', borderwidth=2)
        self.date_entry.pack()

        # Contenedor derecho para la hora y la descripción
        frame_right = tk.Frame(frame_main)
        frame_right.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        tk.Label(frame_right, text="Hora:").grid(row=0, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(frame_right, width=10)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_right, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_right, width=30)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botón para agregar eventos, ubicado en su posición original
        self.add_button = tk.Button(root, text="Agregar Evento", command=self.add_event)
        self.add_button.pack(pady=5)

        # Contenedor para la lista de eventos
        frame_list = tk.Frame(root)
        frame_list.pack(pady=10)

        self.tree = ttk.Treeview(frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Contenedor para los botones de acciones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        self.edit_button = tk.Button(frame_buttons, text="Editar Evento", command=self.edit_event)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        self.del_button = tk.Button(frame_buttons, text="Eliminar Evento", command=self.delete_event)
        self.del_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(frame_buttons, text="Salir", command=self.exit_app)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        # Cargar eventos desde archivo CSV
        self.load_events()

    def add_event(self):
        """Añade un nuevo evento a la lista"""
        date = self.date_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()

        if not date or not time or not desc:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        self.tree.insert("", "end", values=(date, time, desc))
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_event(self):
        """Elimina el evento seleccionado"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")
            return
        confirm = messagebox.askyesno("Confirmación", "¿Está seguro de eliminar el evento seleccionado?")
        if confirm:
            self.tree.delete(selected_item)

    def edit_event(self):
        """Edita el evento seleccionado"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para editar")
            return
        item_values = self.tree.item(selected_item, 'values')
        self.date_entry.set_date(item_values[0])
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, item_values[1])
        self.desc_entry.delete(0, tk.END)
        self.desc_entry.insert(0, item_values[2])
        self.tree.delete(selected_item)

    def save_events(self):
        """Guarda los eventos en un archivo CSV"""
        events = self.tree.get_children()
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Fecha", "Hora", "Descripción"])
            for event in events:
                writer.writerow(self.tree.item(event, "values"))

    def load_events(self):
        """Carga los eventos desde un archivo CSV"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                next(reader, None)  # Saltar encabezado
                for row in reader:
                    self.tree.insert("", "end", values=row)

    def exit_app(self):
        """Guarda los eventos y cierra la aplicación"""
        self.save_events()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()