import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        str_year= self._view._txtAnno.value
        if str_year =="":
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un anno", color="red"))
            self._view.update_page()
            return

        try:
            year=int(str_year)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un anno valido", color="red"))
            self._view.update_page()
            return

        if year < 1816 or year > 2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un anno valido (1816-2016)"))
            self._view.update_page()
            return



        self._model.buildGraph(year)
        self.fill_dd()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view._txt_result.controls.append(ft.Text("Elenco degli stati: "))
        for i in self._model._nodes:
            self._view._txt_result.controls.append(ft.Text(f"{self._model.ottieni_grado(i)}"))
        self._view._txt_result.controls.append(ft.Text("="*60))
        self._view._txt_result.controls.append(ft.Text(f"Numero componenti connesse nel grafo: {self._model.get_num_compConnesse()}"))
        self._view.update_page()

    def fill_dd(self):
        self._view._dd_stati.options.clear()
        nodi=self._model.elementi_dd()
        print (len(nodi))
        for i in nodi:
            self._view._dd_stati.options.append(ft.dropdown.Option(text= str(i), key=i.CCode))

        self._view._dd_stati.update()
        self._view.update_page()

    def handleStatiRaggiungibili(self, e):
        self._view._txt_result.controls.clear()
        code= self._view._dd_stati.value
        source= self._model.ottieni_nodo(code)
        conn=self._model.connessa(source)
        if conn is None:
            self._view._txt_result.controls.append(ft.Text("Selezionare uno Stato da cui far partire la ricerca dei confini!", color="red"))
            self._view.update_page()

            return

        for c in conn:
            self._view._txt_result.controls.append(ft.Text(c))

        self._view.update_page()



