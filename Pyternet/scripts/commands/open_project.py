import os, time

def open_project(project_name):
    # On regarde si le nom du projet existe
    try:
        os.chdir(project_name)
        print(f"Projet {project_name} prêt à être utilisé !")
    except FileNotFoundError:
        print(f"FileNotFoundError: Dossier '{project_name}' n'existe pas/syntaxe invalide")
