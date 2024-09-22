"""Database screen."""

import json

# from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen


class DatabaseScreen(MDScreen):
    """Database screen."""

    def on_enter(self):
        """Charge les données JSON lorsque l'écran devient actif."""
        self.load_json_data()

    def load_json_data(self):
        """Load data from json file and display in list."""
        try:
            with open("database.json", encoding="utf-8") as f:
                data = json.load(f)

            self.ids.data_list.clear_widgets()

            for product_dict in data:
                for name, detail in product_dict.items():
                    elem = OneLineListItem(text=name)

                    elem.bind(
                        on_release=lambda instance, name=name, detail=detail: self.on_item_click(
                            name, detail
                        )
                    )

                    self.ids.data_list.add_widget(elem)

            # # Ajouter chaque élément du JSON à la liste
            # for item in data:

            # # Crée un élément de liste avec le libellé
            # elem = OneLineListItem(text=item["libelle"])
            # # Associe les données à cet élément
            # elem.item_data = item
            # # Connecte l'événement on_release à la méthode on_item_click
            # elem.bind(
            #     on_release=lambda instance: self.on_item_click(instance.item_data)
            # )
            # # Ajoute l'élément à la liste
            # self.ids.data_list.add_widget(elem)

        except FileNotFoundError:
            print("Le fichier database.json n'existe pas.")
        except json.JSONDecodeError:
            print("Erreur lors de la lecture du fichier JSON.")

    def on_item_click(self, item_title, item_data):
        """Redirige vers la page d'ajout avec les champs pré-remplis."""
        _ = item_title  # Ignorer temporairement
        _ = item_data  # Ignorer temporairement
        # add_screen = self.manager.get_screen("content_item")
        # add_screen.ids.field_libelle.text = item_title
        # add_screen.ids.field_brand.text = item_data.get("brand", None)
        # add_screen.ids.field_barcode.text = item_data.get("barcode", None)
        # add_screen.ids.field_comment.text = item_data.get("commentaire", None)
        # add_screen.ids.field_note.text = str(item_data.get("note", None))
        self.manager.current = "content_item"
