"""Screen content item."""

# from kivy.lang import Builder

# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.screenmanager import Screen
# from kivymd.app import MDApp
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.card import MDCard
# from kivymd.uix.fitimage import FitImage
# from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

# from kivymd.uix.slider import MDSlider


class ContentItemScreen(MDScreen):
    """Screen content item."""

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def edit_item(self):
        """Edit item.""" ""
        print("Editer l'item")

    def delete_item(self):
        """Delete item."""
        print("Supprimer l'item")
