from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
import json


class SaisieManuelleScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_form(self):
        """Valide les données du formulaire."""
        errors = []

        libelle = self.ids.field_libelle.text
        marque = self.ids.field_brand.text
        barcode = self.ids.field_barcode.text
        note = self.ids.field_note.value

        if not libelle:
            errors.append("Le champ libelle ne peut pas être vide.")
        if not marque:
            errors.append("Le champ marque ne peut pas être vide.")
        if not barcode:
            errors.append("Le champ barcode ne peut pas être vide.")
        if not note:
            errors.append("Le champ note ne peut pas être vide.")

        if errors:
            self.show_errors(errors)
        else:
            self.process_form()

    def show_errors(self, errors):
        """Affiche une boîte de dialogue avec les erreurs de validation."""
        error_message = "\n".join(errors)
        self.dialog = MDDialog(
            title="Erreurs de validation",
            text=error_message,
            buttons=[
                MDRaisedButton(text="OK", on_release=lambda x: self.dialog.dismiss())
            ],
        )
        self.dialog.open()

    def process_form(self):
        """Traite les données si la validation est réussie."""
        unique_key = self.ids.field_libelle.text
        data = {
            "libelle": self.ids.field_libelle.text,
            "marque": self.ids.field_brand.text,
            "barcode": self.ids.field_barcode.text,
            "commentaire": self.ids.field_comment.text,
            "note": self.ids.field_note.value,
        }

        print("Formulaire validé avec succès!")
        print(data)

        try:
            with open("database.json", "r") as fichier:
                donnees = json.load(fichier)
            if isinstance(donnees, dict):
                donnees = [donnees]
        except FileNotFoundError:
            donnees = []

        donnees.append(data)

        try:
            with open("database.json", "w") as fichier:
                json.dump(donnees, fichier, indent=4)
            print("Données enregistrées avec succès.")
            Snackbar(text="Données enregistrées avec succès!").open()
            self.schedule_redirection()

        except Exception as e:
            print(f"Erreur lors de l'enregistrement des données : {e}")

    def schedule_redirection(self):
        """Planifie la redirection vers l'écran d'accueil."""
        self.clock = Clock.schedule_once(self.redirect_to_home, 2)

    def redirect_to_home(self, *args):
        """Redirige vers l'écran d'accueil."""
        self.manager.current = "accueil"
