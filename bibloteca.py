from data_layer import Database
from datetime import datetime, timedelta

class LibrarySystem:
    def __init__(self):
        self.db = Database()

    def registrar_autor(self, nombre, apellido, nacionalidad):
        query = "INSERT INTO autores (nombre, apellido, nacionalidad) VALUES (?, ?, ?)"
        self.db.execute_query(query, (nombre, apellido, nacionalidad))

    def registrar_libro(self, isbn, titulo, genero, ano_publicacion, autor_id, cantidad_disponible):
        query = """
            INSERT INTO libros (isbn, titulo, genero, ano_publicacion, autor_id, cantidad_disponible)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (isbn, titulo, genero, ano_publicacion, autor_id, cantidad_disponible))

    def registrar_usuario(self, nombre, apellido, tipo_usuario, direccion, telefono):
        query = """
            INSERT INTO usuarios (nombre, apellido, tipo_usuario, direccion, telefono)
            VALUES (?, ?, ?, ?, ?)
        """
        self.db.execute_query(query, (nombre, apellido, tipo_usuario, direccion, telefono))

    def prestar_libro(self, usuario_id, isbn):
        # Comprobación de disponibilidad y tipo de usuario
        disponibilidad = self.db.fetch_all("SELECT cantidad_disponible FROM libros WHERE isbn = ?", (isbn,))
        if disponibilidad and disponibilidad[0][0] > 0:
            tipo_usuario = self.db.fetch_all("SELECT tipo_usuario FROM usuarios WHERE id = ?", (usuario_id,))[0][0]
            prestamos_usuario = len(self.db.fetch_all("SELECT id FROM prestamos WHERE usuario_id = ?", (usuario_id,)))
            limite_prestamos = 3 if tipo_usuario == "estudiante" else 5

            if prestamos_usuario < limite_prestamos:
                fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
                fecha_devolucion = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                self.db.execute_query("""
                    INSERT INTO prestamos (usuario_id, isbn, fecha_prestamo, fecha_devolucion)
                    VALUES (?, ?, ?, ?)
                """, (usuario_id, isbn, fecha_prestamo, fecha_devolucion))
                self.db.execute_query("UPDATE libros SET cantidad_disponible = cantidad_disponible - 1 WHERE isbn = ?", (isbn,))
            else:
                print(f"El usuario {tipo_usuario} ha alcanzado el límite de préstamos.")

    def devolver_libro(self, prestamo_id):
        prestamo = self.db.fetch_all("SELECT isbn FROM prestamos WHERE id = ?", (prestamo_id,))
        if prestamo:
            isbn = prestamo[0][0]
            self.db.execute_query("DELETE FROM prestamos WHERE id = ?", (prestamo_id,))
            self.db.execute_query("UPDATE libros SET cantidad_disponible = cantidad_disponible + 1 WHERE isbn = ?", (isbn,))

    def cerrar_conexion(self):
        self.db.close()