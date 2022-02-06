# Importation des modules
import os
import time

# Message de bienvenue
print("""----------------------------
BIENVENUE SUR PYTERNET
----------------------------
Pour avoir les instruction à suivre pour créer un projet, tapez 'instru'.
Pour avoir la liste des commandes, tapez 'help'.""")


# Fonctions des commandes
def help():
    print("""\n--------------------------------------------------------
	VOICI LES COMMANDES
--------------------------------------------------------
		\n--- Création de projet ---
 - tools        : Avoir les instruction pour créer un projet.
 - mkproj <nom> : Création d'un projet.
 - init         : initialiser la création d'un projet (effectuer dans le dossier projet).
 		\n--- Ouvrir un projet ---
 - open <nom>   : Ouvrir un projet déjà existant
		\n--- Autres ---
 - cd <dir>     : Changer de répertoire ('..' pour revenir en arrière).
 - mkdir <dir>  : Créer un dossier.
 - exit         : Quitter Pyternet.""")


def tools():
    print("""\n--------------------------------------------------------
	VOICI LES INSTRUCTIONS
--------------------------------------------------------
Pour créer un projet Pyternet, tapez 'new_project'
Si vous avez déjà créé un projet Pyternet, ouvrez-le avec 'open' !""")


def mkproj(project_name):
    print(f"Nous créons votre projet avec le nom '{project_name}'...")
    os.mkdir(f"{project_name}")
    time.sleep(1)
    print("Votre projet a été créé avec succès !")


def open_project(project_name):
    # On regarde si le nom du projet existe
    try:
        os.chdir(project_name)
        print(f"Projet {project_name} prêt à être utilisé !")
        dir.append(project_name)
    except FileNotFoundError:
        print(f"FileNotFoundError: Dossier '{project_name}' n'existe pas/syntaxe invalide")
        pass


def init():
    print("Création de 'index.html'...")
    html_file = open("index.html", "w")
    print("Création de 'style.css'...")
    css_file = open("style.css", "w")
    print("Terminé !")


dir = [""]
# Boucle de détection des commandes
while True:
    # Temps d'attente
    time.sleep(0.2)
    # Demande de commande
    cmd = input("\n[Pyternet{}] > ".format("/".join(dir)))
    # Test d'argument
    match cmd.split():
    # try:
    #     cmd, para = cmd.split()
    # except ValueError:
    #     pass

        # Message d'aide
        case ["help"]:
            help()
        # -- CREATION DE PROJET --
        # Message d'affichage des outils
        case ["tools"]:
            tools()
        # Commande "new_project"
        case ["mkproj", project_name]:
            mkproj(project_name)
        # commende pour ouvrir un projet
        case ["open", project_name]:
            open_project(project_name)
        # commende pour initialiser un projet
        case ["init"]:
            init()

        # -- AUTRES --
        # Se déplacer
        case ["cd", cdir]:
            try:
                os.chdir(cdir)
                # Reculer d'un dossier
                if cdir == "..":
                    dir.pop()
                else:
                    dir.append(cdir)
            except FileNotFoundError:
                print(f"Error: {cdir} do not exists.")
                pass
        # Créer un nouveau dossier
        case ["mkdir", cdir]:
            try:
                os.mkdir(cdir)
            except FileExistsError:
                print(f"Error: '{cdir}' exists")
                pass
        # Quitter la Boucle
        case ["exit"]:
            print("Merci d'avoir utilisé Pyternet !")
            break

        # Erreur
        case _:
            print(f"Oups... Nous n'avons pas trouvé la commande. Réessayez !")
