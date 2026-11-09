from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = f"SELECT * FROM biblioteca"
        cursor.execute(query)
        result = []
        for biblioteca in cursor:
            result.append(Biblioteca(biblioteca["id"], biblioteca["nome"], biblioteca["indirizzo"]))
        cursor.close()
        cnx.close()
        return result