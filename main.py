import json

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import NoTransition, Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy_garden.zbarcam import ZBarCam
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import (MDBottomNavigation,
                                         MDBottomNavigationItem)
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar


class MainScreen(Screen):
    pass


class DetailScreen(Screen):
    pass


class ExampleApp(MDApp):
    dialog = None

    def on_symbols(self, instance, symbols):
        print(symbols)

    def load_json_data(self):
        with open("database.json", "r") as f:
            return json.load(f)

    def find_item_in_json(self, item):
        data = self.load_json_data()
        return data.get(item, "Clé non trouvée")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Brown"

        self.screen_manager = ScreenManager(transition=NoTransition())

        main_screen = MainScreen(name="main")
        detail_screen = DetailScreen(name="detail")

        self.screen_manager.add_widget(main_screen)
        self.screen_manager.add_widget(detail_screen)

        main_layout = BoxLayout(orientation="vertical")

        toolbar = MDTopAppBar(title="Example App")
        toolbar.right_action_items = [
            ["magnify", lambda x: self.on_search_button_press()]
        ]

        main_layout.add_widget(toolbar)

        bottom_navigation = MDBottomNavigation()

        bottom_navigation_item1 = MDBottomNavigationItem(
            name="Base de données",
            text="Base de données",
            icon="database",
        )

        self.data_list = MDList()
        scroll_view = ScrollView()
        scroll_view.add_widget(self.data_list)

        bottom_navigation_item1.add_widget(scroll_view)
        bottom_navigation_item1.bind(on_tab_press=self.on_database_tab_press)

        bottom_navigation.add_widget(bottom_navigation_item1)

        bottom_navigation_item2 = MDBottomNavigationItem(
            name="Saisie manuelle",
            text="Saisie manuelle",
            icon="pen",
        )
        bottom_navigation_item2.add_widget(
            MDBoxLayout(
                MDTextField(
                    hint_text="Enter date",
                    date_format="dd/mm/yyyy",
                ),
                orientation="vertical",
                spacing="20dp",
                adaptive_height=True,
                size_hint_x=0.8,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            ),
        )
        bottom_navigation.add_widget(bottom_navigation_item2)

        bottom_navigation_item3 = MDBottomNavigationItem(
            name="Scanner",
            text="Scanner",
            icon="barcode-scan",
        )

        self.scanner_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        scan_button = MDRaisedButton(
            text="Démarrer le scan",
            pos_hint={"center_x": 0.5},
            on_release=self.start_scan,
        )
        self.scanner_layout.add_widget(scan_button)

        self.zbarcam_layout = BoxLayout(
            orientation="vertical", size_hint_y=None, height=0
        )
        self.zbarcam = ZBarCam()
        self.zbarcam.bind(symbols=self.on_symbols)
        self.zbarcam_layout.add_widget(self.zbarcam)

        self.scanner_layout.add_widget(self.zbarcam_layout)
        bottom_navigation_item3.add_widget(self.scanner_layout)
        bottom_navigation.add_widget(bottom_navigation_item3)

        main_layout.add_widget(bottom_navigation)
        main_screen.add_widget(main_layout)

        return self.screen_manager

    def on_database_tab_press(self, instance):
        data = self.load_json_data()
        self.data_list.clear_widgets()
        for item in data:
            elem = OneLineListItem(text=str(item))
            elem.bind(on_release=self.on_item_click)
            self.data_list.add_widget(elem)

    def on_item_click(self, instance):
        self.show_detail_screen(instance.text)

    def on_search_button_press(self):
        print("Search button pressed")

    def start_scan(self, instance):
        self.zbarcam_layout.height = self.scanner_layout.height
        self.zbarcam_layout.size_hint_y = 1

    def show_detail_screen(self, text):
        element = self.find_item_in_json(text)
        detail_screen = self.screen_manager.get_screen("detail")
        detail_layout = BoxLayout(orientation="vertical")

        detail_toolbar = MDTopAppBar(
            title="Detail",
            left_action_items=[["arrow-left", lambda x: self.show_main_screen()]],
            right_action_items=[["delete", lambda x: self.delete_item()]],
        )
        detail_layout.add_widget(detail_toolbar)

        detail_label1 = MDLabel(text=element.get("name"), halign="center")
        detail_layout.add_widget(detail_label1)

        detail_label2 = MDLabel(text=element.get("barcode"), halign="center")
        detail_layout.add_widget(detail_label2)

        detail_screen.clear_widgets()
        detail_screen.add_widget(detail_layout)
        self.screen_manager.current = "detail"

    def delete_item(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Etes vous sur de vouloir supprimer cet élément ?",
                buttons=[
                    MDFlatButton(
                        text="Annuler",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda _: self.dialog.dismiss(),
                    ),
                    MDFlatButton(
                        text="Supprimer",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

    def show_main_screen(self):
        self.screen_manager.current = "main"


ExampleApp().run()
