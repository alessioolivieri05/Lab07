from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        lista_libri = self._libro_dao.get_libri()
        lista_biblioteche = self._biblioteca_dao.get_biblioteche()

        id_biblio_selezionata = None
        if biblioteca:
            for b in lista_biblioteche:
                if b.nome == biblioteca:
                    id_biblio_selezionata = b.id
                    break

        lista_filtrati = []
        for libro in lista_libri:
            match_genere = (not genere) or (libro.genere == genere)
            match_biblio = (not biblioteca) or (libro.id_biblioteca == id_biblio_selezionata)

            if match_genere and match_biblio:
                lista_filtrati.append(libro)

        return lista_filtrati


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        lista_libri = self._libro_dao.get_libri()
        insieme_generi = set()
        for libro in lista_libri:
            insieme_generi.add(libro.genere)
        lista_generi = list(insieme_generi)
        return lista_generi


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        return self._biblioteca_dao.get_biblioteche()
