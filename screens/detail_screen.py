from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivy.metrics import dp

Builder.load_file("kv/detail_screen.kv")


class DetailScreen(Screen):
    def __init__(self, app, **kwargs):
        super(DetailScreen, self).__init__(**kwargs)
        self.app = app

    def update_screen(self, element):
        detail_layout = BoxLayout(orientation="vertical")

        detail_toolbar = MDTopAppBar(
            title="Detail",
            left_action_items=[["arrow-left", lambda x: self.app.show_main_screen()]],
            right_action_items=[["delete", lambda x: self.app.delete_item()]],
        )
        detail_layout.add_widget(detail_toolbar)

        detail_label1 = MDLabel(text=element.get("name"), halign="center")
        detail_layout.add_widget(detail_label1)

        detail_label2 = MDLabel(text=element.get("barcode"), halign="center")
        detail_layout.add_widget(detail_label2)

        # Création du MDBoxLayout pour aligner horizontalement l'icône et le label
        h_layout = MDBoxLayout(
            orientation="horizontal", size_hint_y=None, height=dp(48), spacing=dp(10)
        )

        # Ajout de l'icône
        icon_button = MDIconButton(
            icon="barcode", size_hint=(None, None), size=(dp(24), dp(24))
        )
        h_layout.add_widget(icon_button)

        # Ajout du label
        label = MDLabel(text="Home", halign="center", size_hint_y=None, height=dp(24))
        h_layout.add_widget(label)

        # Ajout du MDBoxLayout au layout principal
        detail_layout.add_widget(h_layout)

        self.clear_widgets()
        self.add_widget(detail_layout)
