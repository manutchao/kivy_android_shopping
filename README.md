# kivy_android_shopping

## Capture d'écran

![Screenshot](lien_vers_une_capture_d_ecran.png)

## Installation

### Prérequis

- Python 3.10
- Kivy
- KivyMD
- Android SDK (pour la compilation sur Android)
- Buildozer
- Cython

### Cloner le projet

```bash
   git clone https://github.com/manutchao/kivy_android_shopping.git
   cd kivy_android_shopping
```

## Installation des dépendances

```bash
   pip install pipenv
   pipenv --python 3.10
   pipenv install
```

## Exécution de l'appli sur le bureau

```bash
   pipenv run python main.py
```

## Compilation pour Android

```bash
   pip install buildozer
   buildozer -v android debug
```

## Structure du projet

```bash
    kivy_android_shopping/

    │
    ├── bin
    ├── buildozer.spec         # Fichier de configuration de Buildozer
    ├── database.json          # Base de données de l'appli
    ├── kv                     # Fichiers .kv pour la définition de l'interface utilisateur
    ├── libs                   # Répertoire contenir des bibliothèques permettant d'assuer la compatibilité de l'appli avec différentes versions d'android
    ├── main.py                # Point d'entrée principal de l'application
    ├── Makefile               # Fichier utilisé pour automatiser certaines tâches
    ├── Pipfile                # Liste des dépendances Python
    ├── Pipfile.lock           # Version verrouillée des dépendances Python
    ├── python-for-android     # Permet de compiler des applications Python pour qu'elles puissent s'exécuter sur des appareils Android
    ├── README.md              # Documentation du projet
    └── screens                # Interfaces graphiques de l'appli
```
