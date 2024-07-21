from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy_garden.zbarcam import ZBarCam

Builder.load_file("kv/main_screen.kv")


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.app = None  # Initialize the app attribute

    def set_app(self, app):
        self.app = app
        # Binding symbols to the app's on_symbols method after the app is set
        self.zbarcam.bind(symbols=self.app.on_symbols)

    def on_kv_post(self, base_widget):
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
        self.zbarcam_layout.add_widget(self.zbarcam)

        self.scanner_layout.add_widget(self.zbarcam_layout)
        bottom_navigation_item3.add_widget(self.scanner_layout)
        bottom_navigation.add_widget(bottom_navigation_item3)

        main_layout.add_widget(bottom_navigation)
        self.add_widget(main_layout)

    def on_database_tab_press(self, instance):
        data = self.app.load_json_data()
        self.data_list.clear_widgets()
        for item in data:
            elem = OneLineListItem(text=str(item))
            elem.bind(on_release=self.on_item_click)
            self.data_list.add_widget(elem)

    def on_item_click(self, instance):
        self.app.show_detail_screen(instance.text)

    def on_search_button_press(self):
        print("Search button pressed")

    def start_scan(self, instance):
        self.zbarcam_layout.height = self.scanner_layout.height
        self.zbarcam_layout.size_hint_y = 1
