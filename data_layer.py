# data_layer.py
import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="library.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                nacionalidad TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                isbn TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                genero TEXT,
                ano_publicacion INTEGER,
                autor_id INTEGER,
                cantidad_disponible INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES autores(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                tipo_usuario TEXT CHECK(tipo_usuario IN ('estudiante', 'profesor')) NOT NULL,
                direccion TEXT,
                telefono TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestamos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                isbn TEXT,
                fecha_prestamo TEXT,
                fecha_devolucion TEXT,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (isbn) REFERENCES libros(isbn)
            )
        """)
        self.connection.commit()

    def execute_query(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def fetch_all(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def close(self):
        self.connection.close()