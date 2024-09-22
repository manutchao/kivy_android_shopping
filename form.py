# import logging
# import os

# from jnius import autoclass
# from kivy.lang import Builder
# from kivy.metrics import dp
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.image import Image
# from kivy.utils import platform
# from kivymd.app import MDApp
# from kivymd.uix.snackbar import Snackbar

# if platform == "android":
#     from android import activity
#     from android.permissions import Permission, request_permissions
#     from android.storage import app_storage_path

#     request_permissions(
#         [
#             Permission.READ_EXTERNAL_STORAGE,
#             Permission.WRITE_EXTERNAL_STORAGE,
#             Permission.CAMERA,
#         ]
#     )


# KV = """
# BoxLayout:
#     orientation: 'vertical'
#     spacing: dp(10)

#     ScrollView:
#         size_hint: (1, 1)
#         do_scroll_x: False
#         do_scroll_y: True

#         BoxLayout:
#             orientation: 'vertical'
#             size_hint_y: None
#             height: self.minimum_height
#             spacing: dp(10)

#             MDTextField:
#                 id: field_libelle
#                 hint_text: "Saisir libellé"
#                 mode: "rectangle"
#                 size_hint_y: None
#                 height: dp(50)

#             MDTextField:
#                 id: field_brand
#                 hint_text: "Saisir marque"
#                 mode: "rectangle"
#                 size_hint_y: None
#                 height: dp(50)

#             MDTextField:
#                 id: field_barcode
#                 hint_text: "Saisir code-barres"
#                 mode: "rectangle"
#                 size_hint_y: None
#                 height: dp(50)

#             MDTextField:
#                 id: field_comment
#                 hint_text: "Saisir commentaire"
#                 mode: "rectangle"
#                 multiline: True
#                 size_hint_y: None
#                 height: dp(100)

#             MDLabel:
#                 text: "Sélectionner une note de 1 à 10"
#                 halign: "center"
#                 size_hint_y: None
#                 height: dp(40)

#             MDSlider:
#                 id: field_note
#                 min: 1
#                 max: 10
#                 value: 5
#                 step: 1
#                 size_hint_y: None
#                 height: dp(50)

#             BoxLayout:
#                 orientation: 'vertical'
#                 size_hint_y: None
#                 height: dp(200)
#                 spacing: dp(10)

#                 MDLabel:
#                     text: "Ajouter une photo"
#                     halign: "center"
#                     size_hint_y: None
#                     height: dp(40)

#                 Image:
#                     id: image_preview
#                     source: ''
#                     size_hint: (1, 1)
#                     fit_mode: 'fill'

#                 BoxLayout:
#                     orientation: 'horizontal'
#                     size_hint_y: None
#                     height: dp(50)
#                     spacing: dp(10)

#                     MDIconButton:
#                         icon: 'image'
#                         theme_icon_color: "Custom"
#                         icon_color: "blue"
#                         on_release: app.choose_photo()

#                     MDIconButton:
#                         icon: 'camera'
#                         theme_icon_color: "Custom"
#                         icon_color: "blue"
#                         on_release: app.take_photo()

#             BoxLayout:
#                 orientation: 'horizontal'
#                 size_hint_y: None
#                 height: dp(50)
#                 spacing: dp(20)
#                 pos_hint: {"center_x": 0.5}

#                 MDRectangleFlatButton:
#                     text: "Valider"
#                     theme_text_color: "Custom"
#                     text_color: "white"
#                     line_color: "green"
#                     size_hint_x: None
#                     width: dp(150)
#                     on_release: app.validate_form()

#                 MDRectangleFlatButton:
#                     text: "Effacer"
#                     theme_text_color: "Custom"
#                     text_color: "white"
#                     line_color: "red"
#                     size_hint_x: None
#                     width: dp(150)
#                     on_release: app.reset()
# """


# class MainScreen(BoxLayout):
#     pass


# class MainApp(MDApp):
#     def build(self):
#         if platform == "android":
#             from android import activity

#             activity.bind(on_activity_result=self.on_activity_result)

#         self.theme_cls.theme_style = "Dark"
#         self.theme_cls.primary_palette = "Brown"
#         self.title = "Kivy_android_shopping"
#         self.img_uri = None
#         return Builder.load_string(KV)

#     def choose_photo(self):
#         if platform == "android":
#             # Utiliser Intent pour ouvrir la galerie
#             Intent = autoclass("android.content.Intent")
#             PythonActivity = autoclass("org.kivy.android.PythonActivity")

#             intent = Intent(Intent.ACTION_PICK)
#             intent.setType("image/*")

#             PythonActivity.mActivity.startActivityForResult(intent, 1)

#         else:
#             Snackbar(
#                 text="Cette fonctionnalité est disponible uniquement sur Android."
#             ).open()

#     def take_photo(self):
#         if platform == "android":
#             request_permissions(
#                 [
#                     Permission.CAMERA,
#                     Permission.WRITE_EXTERNAL_STORAGE,
#                     Permission.READ_EXTERNAL_STORAGE,
#                 ],
#                 self.on_permissions_callback,
#             )
#         else:
#             logging.debug("This functionnality is only available on Android")
#             Snackbar(text="This functionnality is only available on Android").open()

#     def on_permissions_callback(self, permissions, grants):
#         if all(grants):
#             self.capture_photo()
#         else:
#             Snackbar(text="Permissions refusées").open()

#     def capture_photo(self):
#         from jnius import autoclass, cast

#         # Importer les classes nécessaires
#         FileProvider = autoclass("androidx.core.content.FileProvider")
#         Intent = autoclass("android.content.Intent")
#         Uri = autoclass("android.net.Uri")
#         File = autoclass("java.io.File")
#         Environment = autoclass("android.os.Environment")
#         MediaStore = autoclass("android.provider.MediaStore")
#         PythonActivity = autoclass("org.kivy.android.PythonActivity")

#         # Chemin du fichier pour enregistrer la photo
#         file_path = os.path.join(
#             PythonActivity.mActivity.getExternalFilesDir(
#                 Environment.DIRECTORY_PICTURES
#             ).getAbsolutePath(),
#             "myphoto.jpg",
#         )

#         file_path2 = os.path.join(
#             PythonActivity.mActivity.getExternalFilesDir(None).getAbsolutePath(),
#             "testfile.txt",
#         )
#         with open(file_path2, "w") as f:
#             f.write("Test content")
#         if os.path.exists(file_path2):
#             logging.info(f"File created successfully at {file_path2}")
#         else:
#             logging.error("Failed to create file")
#         logging.debug(f"File path : {file_path}")

#         photo_file = File(file_path)
#         if not photo_file.exists():
#             try:
#                 photo_file.createNewFile()
#                 logging.info(f"File created at {file_path}")
#             except Exception as e:
#                 logging.error(f"Failed to create file: {e}")

#         # Créer un URI pour le fichier avec FileProvider
#         authority = (
#             "org.test.trackerapp.fileprovider"  # Remplacez par votre propre autorité
#         )
#         uri = FileProvider.getUriForFile(
#             PythonActivity.mActivity, authority, photo_file
#         )

#         self.img_uri = uri

#         # Création d'un intent pour capturer une image
#         intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)

#         # Ajout de l'URI au contenu de l'intent (converti en chaîne avec toString())
#         intent.putExtra(
#             MediaStore.EXTRA_OUTPUT, uri.toString()
#         )  # Conversion de l'URI en chaîne

#         intent.addFlags(
#             Intent.FLAG_GRANT_WRITE_URI_PERMISSION
#         )  # Autoriser la permission d'écriture sur l'URI

#         # Vérifier si l'intent de capture d'image peut être géré
#         package_manager = PythonActivity.mActivity.getPackageManager()
#         if intent.resolveActivity(package_manager) is not None:
#             logging.info("Launching camera...")
#             PythonActivity.mActivity.startActivityForResult(intent, 0)
#             logging.info("No camera app available...")
#         else:
#             Snackbar(text="Caméra non disponible").open()

#     def on_activity_result(self, request_code, result_code, data):
#         logging.info("on_activity_result called")
#         logging.info(f"[request_code] {request_code}, result_code: {result_code}")

#         if platform == "android":
#             if request_code == 0 and result_code == -1:  # Photo capturée avec succès
#                 logging.info("Photo capture succeeded!")
#                 if self.img_uri is not None:
#                     # Afficher l'URI de l'image pour vérifier qu'elle est bien présente
#                     logging.info(f"Image URI: {self.img_uri.toString()}")

#                     # Mettre à jour l'aperçu de l'image avec l'URI stocké
#                     self.root.ids.image_preview.source = self.img_uri.toString()

#                     # Vérifier si l'image source est correctement mise à jour
#                     logging.info(
#                         f"Image source updated to: {self.root.ids.image_preview.source}"
#                     )
#                 else:
#                     logging.warning("Image URI is None")
#             elif (
#                 request_code == 1 and result_code == -1
#             ):  # Photo sélectionnée dans la galerie
#                 if data is not None:
#                     uri = data.getData()
#                     # Afficher l'URI de la galerie pour vérifier qu'elle est bien présente
#                     logging.info(f"Gallery image URI: {uri.toString()}")

#                     # Mettre à jour l'aperçu de l'image avec l'URI sélectionnée
#                     self.root.ids.image_preview.source = uri.toString()

#                     # Vérifier si l'image source est correctement mise à jour
#                     logging.info(
#                         f"Image source updated to: {self.root.ids.image_preview.source}"
#                     )

#     def validate_form(self):
#         libelle = self.root.ids.field_libelle.text.strip()
#         marque = self.root.ids.field_brand.text.strip()
#         barcode = self.root.ids.field_barcode.text.strip()
#         commentaire = self.root.ids.field_comment.text.strip()
#         note = self.root.ids.field_note.value

#         if not libelle or not marque or not barcode:
#             Snackbar(text="Veuillez remplir tous les champs obligatoires.").open()
#         else:
#             logging.info("Form validate with success")
#             Snackbar(text="Formulaire validé avec succès !").open()

#     def reset(self):
#         logging.info("Reset fields")
#         self.root.ids.field_libelle.text = ""
#         self.root.ids.field_brand.text = ""
#         self.root.ids.field_barcode.text = ""
#         self.root.ids.field_comment.text = ""
#         self.root.ids.field_note.value = 5
#         self.root.ids.image_preview.source = ""


# if __name__ == "__main__":
#     MainApp().run()
