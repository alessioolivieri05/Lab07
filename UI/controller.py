import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dd_generi(self):
        lista_generi = self._model.get_generi()
        for genere in lista_generi:
            self._view.dd_generi.options.append(ft.dropdown.Option(genere))

    def popola_dd_biblioteche(self):
        lista_biblioteche = self._model.get_biblioteche()
        for biblioteca in lista_biblioteche:
            self._view.dd_biblioteche.options.append(ft.dropdown.Option(biblioteca.nome))

    # CALLBACKS DROPDOWN
    # TODO
    def cambia_genere(self, e):
        self.genere_selezionato = self._view.dd_generi.value

    def cambia_biblioteca(self, e):
        self.biblioteca_selezionata = self._view.dd_biblioteche.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self,e):
        self._view.list_view.controls.clear()
        lista_filtrati=self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if not lista_filtrati:
            self._view.list_view.controls.append(ft.Text("Nessun libro trovato con i filtri selezionati.", color="red"))
        else:
            for libro in lista_filtrati:
                testo_libro = f"{libro.titolo} - {libro.autore} ({libro.genere})"
                self._view.list_view.controls.append(ft.Text(testo_libro))
        self._view.list_view.update()
