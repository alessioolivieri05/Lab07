from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_libri(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = f"SELECT * FROM libro"
        cursor.execute(query)
        righe_db = cursor.fetchall()
        result = []
        for libro in righe_db:
            result.append(Libro(libro["id"], libro["titolo"], libro["autore"], libro["genere"],
                                libro["anno_pubblicazione"], libro["id_biblioteca"]))
        cursor.close()
        cnx.close()
        return result
