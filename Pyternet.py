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
    try:
        cmd, para = cmd.split()
    except ValueError:
        pass

    # Message d'aide
    if cmd == "help":
        help()
    # -- CREATION DE PROJET --
    # Message d'affichage des outils
    elif cmd == "tools":
        tools()
    # Commande "new_project"
    elif cmd == "mkproj":
        mkproj(para)
    # commende pour ouvrir un projet
    elif cmd == "open":
        open_project(para)
    # commende pour initialiser un projet
    elif cmd == "init":
        init()

    # -- AUTRES --
    # Se déplacer
    elif cmd == "cd":
        try:
            os.chdir(para)
            # Reculer d'un dossier
            if para == "..":
                dir.pop()
            else:
                dir.append(para)
        except FileNotFoundError:
            print(f"Error: {para} do not exists.")
            pass
    # Créer un nouveau dossier
    elif cmd == "mkdir":
        try:
            os.mkdir(para)
        except FileExistsError:
            print(f"Error: '{para}' exists")
            pass
    # Quitter la Boucle
    elif cmd == "exit":
        break

    # Erreur
    else:
        print(f"Oups... Nous n'avons pas trouvé la commande '{cmd}'. Réessayez !")
