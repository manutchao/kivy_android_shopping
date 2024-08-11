from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy_garden.zbarcam import ZBarCam


class ScannerScreen(MDScreen):
    def __init__(self, app=None, **kwargs):
        super(ScannerScreen, self).__init__(**kwargs)
        self.app = app

        if self.app:
            self.ids.zbarcam.bind(symbols=self.app.on_symbols)

    def start_scan(self, instance):
        """Démarre le scanner en ajustant la hauteur du layout du scanner."""
        self.ids.zbarcam_layout.height = self.height
        self.ids.zbarcam_layout.size_hint_y = 1
