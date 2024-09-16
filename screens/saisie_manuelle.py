import json
import logging
import os
import secrets
import string

from jnius import autoclass
from kivy.clock import Clock
from kivy.utils import platform
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

if platform == "android":
    from android.permissions import Permission, request_permissions

    request_permissions(
        [
            Permission.READ_EXTERNAL_STORAGE,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.CAMERA,
        ]
    )


# def generate_file_name(extension=".jpg", longueur=10):
#     caracteres = string.ascii_letters + string.digits
#     nom_fichier = "".join(random.choice(caracteres) for _ in range(longueur))
#     return nom_fichier + extension


def generate_file_name(extension=".jpg", longueur=10):
    caracteres = string.ascii_letters + string.digits
    nom_fichier = "".join(secrets.choice(caracteres) for _ in range(longueur))
    return nom_fichier + extension


class SaisieManuelleScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform == "android":
            from android import activity

            activity.bind(on_activity_result=self.on_activity_result)

    def photo_taken(self, path):
        # Mettre à jour l'image affichée avec la photo prise
        self.ids.image_preview.source = path

    def photo_chosen(self, path):
        # Mettre à jour l'image affichée avec la photo sélectionnée
        self.ids.image_preview.source = path[0]  # `path` est une liste

    def choose_photo(self):
        if platform == "android":
            # Utiliser Intent pour ouvrir la galerie
            Intent = autoclass("android.content.Intent")
            PythonActivity = autoclass("org.kivy.android.PythonActivity")

            intent = Intent(Intent.ACTION_PICK)
            intent.setType("image/*")

            PythonActivity.mActivity.startActivityForResult(intent, 1)

        else:
            Snackbar(text="Functionnality only available on Android").open()

    def take_photo(self):
        if platform == "android":
            request_permissions(
                [
                    Permission.CAMERA,
                    Permission.WRITE_EXTERNAL_STORAGE,
                    Permission.READ_EXTERNAL_STORAGE,
                ],
                self.on_permissions_callback,
            )
        else:
            logging.debug("This functionnality is only available on Android")
            Snackbar(text="Functionnality only available on Android").open()

    def on_permissions_callback(self, permissions, grants):
        if all(grants):
            self.capture_photo()
        else:
            Snackbar(text="Permissions refusées").open()

    # def capture_photo(self):
    #     from jnius import autoclass
    #     from jnius import cast

    #     # Importer les classes nécessaires
    #     FileProvider = autoclass("androidx.core.content.FileProvider")
    #     Intent = autoclass("android.content.Intent")
    #     Uri = autoclass("android.net.Uri")
    #     File = autoclass("java.io.File")
    #     Environment = autoclass("android.os.Environment")
    #     MediaStore = autoclass("android.provider.MediaStore")
    #     PythonActivity = autoclass("org.kivy.android.PythonActivity")

    #     # Chemin du fichier pour enregistrer la photo
    #     file_path = os.path.join(
    #         PythonActivity.mActivity.getExternalFilesDir(
    #             Environment.DIRECTORY_PICTURES
    #         ).getAbsolutePath(),
    #         generate_file_name(),
    #     )
    #     logging.debug(f"File path : {file_path}")

    #     photo_file = File(file_path)
    #     if not photo_file.exists():
    #         try:
    #             photo_file.createNewFile()
    #             logging.info(f"File created at {file_path}")
    #         except Exception as e:
    #             logging.error(f"Failed to create file: {e}")

    #     # Créer un URI pour le fichier avec FileProvider
    #     authority = (
    #         "org.test.trackerapp.fileprovider"
    #     )
    #     uri = FileProvider.getUriForFile(
    #         PythonActivity.mActivity, authority, photo_file
    #     )

    #     self.img_uri = uri

    #     # Création d'un intent pour capturer une image
    #     intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)

    #     logging.info(f"Type of uri: {type(uri)}")

    #     # Ajout de l'URI au contenu de l'intent
    #     intent.putExtra(MediaStore.EXTRA_OUTPUT, uri)

    #     # # Ajout de l'URI au contenu de l'intent
    #     # intent.putExtra(
    #     #     MediaStore.EXTRA_OUTPUT, uri.toString()
    #     # )  # Conversion de l'URI en chaîne

    #     intent.addFlags(
    #         Intent.FLAG_GRANT_WRITE_URI_PERMISSION
    #         | Intent.FLAG_GRANT_READ_URI_PERMISSION
    #     )  # Autoriser la permission d'écriture sur l'URI

    #     # Vérifier si l'intent de capture d'image peut être géré
    #     package_manager = PythonActivity.mActivity.getPackageManager()
    #     if intent.resolveActivity(package_manager) is not None:
    #         logging.info("Launching camera...")
    #         PythonActivity.mActivity.startActivityForResult(intent, 0)
    #         logging.info("No camera app available...")
    #     else:
    #         Snackbar(text="Caméra non disponible").open()

    def capture_photo(self):
        from jnius import autoclass

        # Importer les classes nécessaires
        FileProvider = autoclass("androidx.core.content.FileProvider")
        Intent = autoclass("android.content.Intent")
        File = autoclass("java.io.File")
        Environment = autoclass("android.os.Environment")
        MediaStore = autoclass("android.provider.MediaStore")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")

        # Chemin du fichier pour enregistrer la photo
        file_path = os.path.join(
            PythonActivity.mActivity.getExternalFilesDir(
                Environment.DIRECTORY_PICTURES
            ).getAbsolutePath(),
            generate_file_name(),
        )
        logging.debug(f"File path : {file_path}")

        # Création du fichier
        photo_file = File(file_path)
        if not photo_file.exists():
            try:
                photo_file.createNewFile()
                logging.info(f"File created at {file_path}")
            except Exception as e:
                logging.error(f"Failed to create file: {e}")
                return  # Arrêter si la création échoue

        # Créer un URI pour le fichier avec FileProvider
        authority = "org.test.trackerapp.fileprovider"
        uri = FileProvider.getUriForFile(
            PythonActivity.mActivity, authority, photo_file
        )

        self.img_uri = uri

        # Création de l'intent pour capturer une image
        intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)

        # Ajout de l'URI à l'intent sans conversion en chaîne
        intent.putExtra(MediaStore.EXTRA_OUTPUT, uri.toString())

        # Accorder les permissions URI
        intent.addFlags(
            Intent.FLAG_GRANT_WRITE_URI_PERMISSION
            | Intent.FLAG_GRANT_READ_URI_PERMISSION
        )

        # Vérifier si l'intent de capture d'image peut être géré
        package_manager = PythonActivity.mActivity.getPackageManager()
        if intent.resolveActivity(package_manager) is not None:
            logging.info("Launching camera...")
            PythonActivity.mActivity.startActivityForResult(intent, 0)
        else:
            logging.info("No camera app available...")
            Snackbar(text="Caméra non disponible").open()

    def on_activity_result(self, request_code, result_code, data):
        logging.info("on_activity_result called")
        logging.info(f"[request_code] {request_code}")
        logging.info(f"result_code: {result_code}")

        if platform == "android":
            if request_code == 0 and result_code == -1:
                logging.info("Photo capture succeeded!")
                if self.img_uri is not None:
                    logging.info(f"Image URI: {self.img_uri.toString()}")

                # Mettre à jour l'aperçu de l'image avec l'URI
                self.ids.image_preview.source = self.img_uri.toString()

    # def on_activity_result(self, request_code, result_code, data):
    #     logging.info("on_activity_result called")
    #     logging.info(f"[request_code] {request_code}")
    #     logging.info(f"result_code: {result_code}")

    #     if platform == "android":
    #         if request_code == 0 and result_code == -1:
    #             logging.info("Photo capture succeeded!")
    #             if self.img_uri is not None:
    #                 logging.info(f"Image URI: {self.img_uri.toString()}")
    #                 self.ids.image_preview.source = self.img_uri.toString()
    #                 logging.info(
    #                     f"Img updated to: {self.ids.image_preview.source}"
    #                 )
    #             else:
    #                 logging.warning("Image URI is None")
    #         elif (
    #             request_code == 1 and result_code == -1
    #         ):
    #             if data is not None:
    #                 uri = data.getData()
    #                 logging.info(f"Gallery image URI: {uri.toString()}")
    #                 self.ids.image_preview.source = uri.toString()
    #                 logging.info(
    #                     f"Img updated to: {self.ids.image_preview.source}"
    #                 )

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
            unique_key: {
                "libelle": self.ids.field_libelle.text,
                "marque": self.ids.field_brand.text,
                "barcode": self.ids.field_barcode.text,
                "commentaire": self.ids.field_comment.text,
                "note": self.ids.field_note.value,
            }
        }

        print("Formulaire validé avec succès!")
        print(data)

        try:
            with open("database.json", "r") as fichier:
                donnees = json.load(fichier)
            if isinstance(donnees, dict):
                donnees.update(data)
            elif isinstance(donnees, list):
                if len(donnees) > 0 and isinstance(donnees[0], dict):
                    donnees[0].update(data)
                else:
                    donnees.append(data)
            else:
                raise ValueError("Invalid data format json file")
        except FileNotFoundError:
            donnees = data
        except ValueError as e:
            print(f"Erreur de format de données : {e}")
            return

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
