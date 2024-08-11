from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar

from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem


from screens.accueil import AccueilScreen
from screens.database import DatabaseScreen
from screens.saisie_manuelle import SaisieManuelleScreen
from screens.scanner import ScannerScreen


class MyScreenManager(ScreenManager):
    pass


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Brown"
        self.title = "MKivy_andoid__shopping"
        # Window.size = (360, 640)
        Builder.load_file("kv/accueil.kv")
        Builder.load_file("kv/database.kv")
        Builder.load_file("kv/saisie_manuelle.kv")
        Builder.load_file("kv/scanner.kv")
        return Builder.load_file("kv/main.kv")


if __name__ == "__main__":
    MainApp().run()


# import json
# import logging
# from kivy.uix.screenmanager import NoTransition, ScreenManager
# from kivymd.app import MDApp
# from screens.main_screen import MainScreen
# from screens.detail_screen import DetailScreen
# from screens.add_screen import AddScreen
# from kivymd.uix.dialog import MDDialog
# from kivymd.uix.button import MDFlatButton, MDRaisedButton

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# class AndroidApp(MDApp):
#     dialog = None

#     def build(self):
#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Brown"

#         self.screen_manager = ScreenManager(transition=NoTransition())

#         main_screen = MainScreen(name="main")
#         main_screen.set_app(self)
#         detail_screen = DetailScreen(app=self, name="detail")
#         add_screen = AddScreen(app=self, name="add")

#         self.screen_manager.add_widget(main_screen)
#         self.screen_manager.add_widget(detail_screen)
#         self.screen_manager.add_widget(add_screen)

#         # Pass the app instance to the screens
#         main_screen.set_app(self)

#         return self.screen_manager

#     def on_symbols(self, instance, symbols):
#         print(symbols)
#         barcode = ""
#         if symbols:
#             for symbol in symbols:
#                 data_value = symbol.data
#                 barcode = data_value.decode("utf-8")
#         print(barcode)

#         if self.find_item_in_json_by_barcode(barcode):
#             print(self.find_item_in_json_by_barcode(barcode))
#             self.show_detail_screen(
#                 self.find_item_in_json_by_barcode(barcode).get("name")
#             )
#             logger.info("Article found")
#         else:
#             self.dialog = MDDialog(text=f"L'article scanné {barcode} n'existe pas")
#             logger.info("Article not found")
#         self.dialog.open()

#     def load_json_data(self):
#         with open("database.json", "r") as f:
#             return json.load(f)

#     def find_item_in_json_by_barcode(self, barcode):
#         data = self.load_json_data()
#         for key, value in data.items():
#             if value.get("barcode") == barcode:
#                 print(value)
#                 return value
#         return None

#     def find_item_in_json(self, item):
#         data = self.load_json_data()
#         return data.get(item, "Clé non trouvée")

#     def show_detail_screen(self, text):
#         element = self.find_item_in_json(text)
#         detail_screen = self.screen_manager.get_screen("detail")
#         detail_screen.update_screen(element)
#         self.screen_manager.current = "detail"

#     def show_main_screen(self):
#         self.screen_manager.current = "main"

#     def delete_item(self):
#         if not self.dialog:
#             self.dialog = MDDialog(
#                 text="Etes vous sur de vouloir supprimer cet élément ?",
#                 buttons=[
#                     MDFlatButton(
#                         text="Annuler",
#                         theme_text_color="Custom",
#                         text_color=self.theme_cls.primary_color,
#                         on_release=lambda _: self.dialog.dismiss(),
#                     ),
#                     MDFlatButton(
#                         text="Supprimer",
#                         theme_text_color="Custom",
#                         text_color=self.theme_cls.primary_color,
#                         on_release=lambda _: print("suppression !!!!!"),
#                     ),
#                 ],
#             )
#         self.dialog.open()


# if __name__ == "__main__":
#     AndroidApp().run()
