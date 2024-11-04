# app.py
import tkinter as tk
from tkinter import messagebox
from bibloteca import LibrarySystem
from tkinter import Toplevel

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca")
        
        # Inicializar el sistema de biblioteca (capa de negocio)
        self.library_system = LibrarySystem()
        
        # Configurar el menú principal
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Menú de Gestión
        gestion_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Gestión", menu=gestion_menu)
        gestion_menu.add_command(label="Gestión de Biblioteca", command=self.abrir_gestion_biblioteca)
        gestion_menu.add_command(label="Gestión de Usuarios", command=self.abrir_gestion_usuarios)
        
        # Menú de Consultas
        consultas_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Consultas", menu=consultas_menu)
        consultas_menu.add_command(label="Consultar Disponibilidad", command=self.abrir_consultas)

    def abrir_gestion_biblioteca(self):
        LibraryAppWindow(self.root, self.library_system)

    def abrir_gestion_usuarios(self):
        UserManagementWindow(self.root, self.library_system)

    def abrir_consultas(self):
        ConsultationsWindow(self.root, self.library_system)

# Crear la ventana de Gestión de Biblioteca
class LibraryAppWindow:
    def __init__(self, root, library_system):
        self.window = Toplevel(root)
        self.window.title("Gestión de Biblioteca")
        self.library_system = library_system

        # Frame de Registro de Libros
        frame_libro = tk.Frame(self.window, padx=10, pady=10)
        frame_libro.grid(row=0, column=0)
        tk.Label(frame_libro, text="Registro de Libro").grid(row=0, column=0, columnspan=2)
        tk.Label(frame_libro, text="ISBN:").grid(row=1, column=0)
        self.entry_isbn_libro = tk.Entry(frame_libro)
        self.entry_isbn_libro.grid(row=1, column=1)
        tk.Label(frame_libro, text="Título:").grid(row=2, column=0)
        self.entry_titulo_libro = tk.Entry(frame_libro)
        self.entry_titulo_libro.grid(row=2, column=1)
        tk.Button(frame_libro, text="Registrar Libro", command=self.registrar_libro).grid(row=4, column=0, columnspan=2)

    def registrar_libro(self):
        isbn = self.entry_isbn_libro.get()
        titulo = self.entry_titulo_libro.get()
        if isbn and titulo:
            self.library_system.registrar_libro(isbn, titulo, "genero", 2023, 1, 5)  # Agrega valores de prueba
            messagebox.showinfo("Éxito", "Libro registrado correctamente.")
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# Crear la ventana de Gestión de Usuarios
class UserManagementWindow:
    def __init__(self, root, library_system):
        self.window = Toplevel(root)
        self.window.title("Gestión de Usuarios")
        self.library_system = library_system

        # Frame de Registro de Usuarios
        frame_usuario = tk.Frame(self.window, padx=10, pady=10)
        frame_usuario.grid(row=0, column=0)
        tk.Label(frame_usuario, text="Registro de Usuario").grid(row=0, column=0, columnspan=2)
        tk.Label(frame_usuario, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre_usuario = tk.Entry(frame_usuario)
        self.entry_nombre_usuario.grid(row=1, column=1)
        tk.Label(frame_usuario, text="Apellido:").grid(row=2, column=0)
        self.entry_apellido_usuario = tk.Entry(frame_usuario)
        self.entry_apellido_usuario.grid(row=2, column=1)
        tk.Label(frame_usuario, text="Tipo de Usuario:").grid(row=3, column=0)
        self.entry_tipo_usuario = tk.Entry(frame_usuario)
        self.entry_tipo_usuario.grid(row=3, column=1)
        tk.Button(frame_usuario, text="Registrar Usuario", command=self.registrar_usuario).grid(row=4, column=0, columnspan=2)

    def registrar_usuario(self):
        nombre = self.entry_nombre_usuario.get()
        apellido = self.entry_apellido_usuario.get()
        tipo_usuario = self.entry_tipo_usuario.get()
        if nombre and apellido and tipo_usuario:
            self.library_system.registrar_usuario(nombre, apellido, tipo_usuario, "direccion", "telefono")  # Agrega valores de prueba
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")

# Crear la ventana de Consultas
class ConsultationsWindow:
    def __init__(self, root, library_system):
        self.window = Toplevel(root)
        self.window.title("Consultas de Disponibilidad")
        self.library_system = library_system

        # Consulta de Disponibilidad
        frame_consulta = tk.Frame(self.window, padx=10, pady=10)
        frame_consulta.grid(row=0, column=0)
        tk.Label(frame_consulta, text="Consultar Disponibilidad de Libros").grid(row=0, column=0, columnspan=2)
        tk.Label(frame_consulta, text="ISBN:").grid(row=1, column=0)
        self.entry_isbn_consulta = tk.Entry(frame_consulta)
        self.entry_isbn_consulta.grid(row=1, column=1)
        tk.Button(frame_consulta, text="Consultar", command=self.consultar_disponibilidad).grid(row=2, column=0, columnspan=2)

    def consultar_disponibilidad(self):
        isbn = self.entry_isbn_consulta.get()
        disponibilidad = self.library_system.db.fetch_all("SELECT cantidad_disponible FROM libros WHERE isbn = ?", (isbn,))
        if disponibilidad:
            messagebox.showinfo("Disponibilidad", f"Cantidad disponible: {disponibilidad[0][0]}")
        else:
            messagebox.showwarning("Error", "El libro no se encontró en el sistema.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()