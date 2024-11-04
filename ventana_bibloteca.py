import tkinter as tk
from tkinter import messagebox
from bibloteca import LibrarySystem

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca")
        self.library_system = LibrarySystem()
        
        # Frame de Registro de Autores
        frame_autor = tk.Frame(root, padx=10, pady=10)
        frame_autor.grid(row=0, column=0)
        tk.Label(frame_autor, text="Registro de Autor").grid(row=0, column=0, columnspan=2)
        tk.Label(frame_autor, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre_autor = tk.Entry(frame_autor)
        self.entry_nombre_autor.grid(row=1, column=1)
        tk.Label(frame_autor, text="Apellido:").grid(row=2, column=0)
        self.entry_apellido_autor = tk.Entry(frame_autor)
        self.entry_apellido_autor.grid(row=2, column=1)
        tk.Label(frame_autor, text="Nacionalidad:").grid(row=3, column=0)
        self.entry_nacionalidad_autor = tk.Entry(frame_autor)
        self.entry_nacionalidad_autor.grid(row=3, column=1)
        tk.Button(frame_autor, text="Registrar Autor", command=self.registrar_autor).grid(row=4, column=0, columnspan=2)

        # Frame de Registro de Libros
        frame_libro = tk.Frame(root, padx=10, pady=10)
        frame_libro.grid(row=0, column=1)
        tk.Label(frame_libro, text="Registro de Libro").grid(row=0, column=0, columnspan=2)
        tk.Label(frame_libro, text="ISBN:").grid(row=1, column=0)
        self.entry_isbn_libro = tk.Entry(frame_libro)
        self.entry_isbn_libro.grid(row=1, column=1)
        tk.Label(frame_libro, text="Título:").grid(row=2, column=0)
        self.entry_titulo_libro = tk.Entry(frame_libro)
        self.entry_titulo_libro.grid(row=2, column=1)
        tk.Button(frame_libro, text="Registrar Libro", command=self.registrar_libro).grid(row=4, column=0, columnspan=2)

    def registrar_autor(self):
        nombre = self.entry_nombre_autor.get()
        apellido = self.entry_apellido_autor.get()
        nacionalidad = self.entry_nacionalidad_autor.get()
        if nombre and apellido and nacionalidad:
            self.library_system.registrar_autor(nombre, apellido, nacionalidad)
            messagebox.showinfo("Éxito", "Autor registrado correctamente.")
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")

    def registrar_libro(self):
        isbn = self.entry_isbn_libro.get()
        titulo = self.entry_titulo_libro.get()
        # Completar con los campos faltantes
        # Luego usar library_system.registrar_libro(...)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()