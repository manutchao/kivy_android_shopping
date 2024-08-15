from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
import json
from kivy.uix.screenmanager import ScreenManager, Screen


class DatabaseScreen(MDScreen):
    def on_enter(self):
        """Charge les données JSON lorsque l'écran devient actif."""
        self.load_json_data()

    def load_json_data(self):
        """Charge les données à partir d'un fichier JSON et les affiche dans la liste."""
        try:
            with open("database.json", "r") as f:
                data = json.load(f)

            self.ids.data_list.clear_widgets()

            for product_dict in data:
                for product_name, details in product_dict.items():

                    # Crée un élément de liste avec le libellé
                    elem = OneLineListItem(text=product_name)

                    # Connecte l'événement on_release à la méthode on_item_click
                    elem.bind(
                        on_release=lambda instance: self.on_item_click(
                            product_name, details
                        )
                    )
                    # Ajoute l'élément à la liste
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
        add_screen = self.manager.get_screen("content_item")
        add_screen.ids.field_libelle.text = item_title
        add_screen.ids.field_brand.text = item_data.get("brand", None)
        add_screen.ids.field_barcode.text = item_data.get("barcode", None)
        add_screen.ids.field_comment.text = item_data.get("commentaire", None)
        add_screen.ids.field_note.text = str(item_data.get("note", None))
        self.manager.current = "content_item"
