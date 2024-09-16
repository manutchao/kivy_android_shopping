# add_screen.py
from kivy.lang import Builder
from kivymd.uix.screen import Screen

Builder.load_file("kv/add_screen.kv")


class AddScreen(Screen):
    def __init__(self, app, **kwargs):
        super(AddScreen, self).__init__(**kwargs)
        self.app = app

    def submit(self, app):
        # Récupérer les champs du formulaire
        libelle = app.root.get_screen("detail_screen").ids.tf_libelle.text
        brand = app.root.get_screen("detail_screen").ids.tf_brand.text
        barcode = app.root.get_screen("detail_screen").ids.tf_barcode.text
        comment = app.root.get_screen("detail_screen").ids.tf_comment.text
        rating = app.root.get_screen("detail_screen").ids.slider.value

        print(f"Libellé: {libelle}")
        print(f"Marque: {brand}")
        print(f"barcode: {barcode}")
        print(f"Comment: {comment}")
        print(f"Note: {rating}")

    def reset(self, app):
        # Réinitialiser les champs du formulaire
        screen = app.root.get_screen("detail_screen")
        screen.ids.tf_libelle.text = ""
        screen.ids.tf_brand.text = ""
        screen.ids.tf_barcode.text = ""
        screen.ids.tf_comment.text = ""
        screen.ids.slider.value = 5
        print("Formulaire réinitialisé")

    def show_main_screen(self, app):
        # Revenir à l'écran principal
        app.root.current = "main_screen"
        print("Retour à l'écran principal")

    def delete_item(self, app):
        # Logique pour supprimer un élément (à adapter selon votre besoin)
        print("Élément supprimé")


# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.uix.screen import Screen
# from kivymd.uix.toolbar import MDTopAppBar
# from kivymd.uix.label import MDLabel
# from kivy.uix.floatlayout import FloatLayout
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.button import MDIconButton, MDRoundFlatIconButton
# from kivy.metrics import dp
# from kivy.uix.slider import Slider

# Builder.load_file("kv/add_screen.kv")


# class DetailScreen(Screen):
#     def __init__(self, app, **kwargs):
#         super(DetailScreen, self).__init__(**kwargs)
#         self.app = app

#     def submit():
#         pass
#         print("ok")

#     def reset():
#         pass
