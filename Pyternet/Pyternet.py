# Modules importation
import os, time

# Commands importation
from scripts.commands import help, instru, mkproj, open_project, new_page, init, config_page

language = ''

inpt = input("""Merci de choisir la langue
Thanks for choice the language :

fra : Français (France)
eng : English

[Pyternet] > """)

while True:
    if inpt == 'fra':
        # Welcome message
        print("""----------------------------
BIENVENUE SUR PYTERNET
----------------------------
Pour avoir les instruction à suivre pour créer un projet, tapez 'instru'.
Pour avoir la liste des commandes, tapez 'help'.

Vous utilisez actuellement Pyternet v1""")
        language = 'fra'
        print("ATTENTION : Vous êtes actuellement dans le dossier avec le code de Pyternet. Pour vous placer ans un autre dossier, tapez la commande \"cd\" ")
        break

    elif inpt == 'eng':
        print("Comming soon !")
        inpt = input()

    else: break
#Boucle de détection des commandes
while language == 'fra':
    #Temps d'attente
    time.sleep(1)
    #Demande de commande
    cmd = input("\n[Pyternet] > ")

    #Command "cmds"
    if cmd == "help":
        help.help()

    #Command "instru"
    elif cmd == "instru":
        try:
            instru.instru()
        except:
            print("Error: Une erreur est survenue...")

    #Command "new_project"
    elif cmd == "mkproj":
        try:
            mkproj.mkproj()
        except:
            print("Error: Une erreur est survenue...")

    #Command open
    elif cmd == "open":
        try:
            project_name = input("Entrez le nom du projet à ouvrir : \n[Pyternet] > ")
            open_project.open_project(project_name=project_name)
        except:
            print("Error: Une erreur est survenue...")

    #Command init
    elif cmd == "init":
        try:
            init.init()
        except:
            print("Error: Une erreur est survenue...")

    #-- GESTION DES PAGES --
    #Command npage
    elif cmd == "npage":
        try:
            cmd = input("Entrez le nom de la page ATTENTION : Sans les caractères \"/ \ : * ? \" < > |\".")
            page_name = cmd + ".html"
            cmd = input("Entrez le titre de la page. ")
            title = cmd
            new_page.new_page(page_name=page_name, title=title)
        except:
            print("Error: Une erreur est survenue...")

    elif cmd == "config_page":
        page_name = input("Quelle page souhaitez-vous configurer ? > ")
        page_name = page_name + ".html"

        try:
            config_page.config_page(page_name=page_name)
        except:
            print("Error: Une erreur est survenue...")

    #-- AUTRES --
    #Command cd
    elif cmd == "cd":
        chdir = input("\n[Pyternet{}:cd] > ")
        try:
            os.chdir(chdir)
            #Reculer d'un dossier
            if chdir == "..":
                dir.pop()
            else:
                dir.append(chdir)
        except FileNotFoundError:
            print(f"Error: {chdir} do not exists.")
            pass
    #Command mkdir
    elif cmd == "mkdir":
        mkdir = input("\n[Pyternet{}:mkdir] > ")
        try:
            os.mkdir(mkdir)
        except FileExistsError:
            print(f"Error: '{mkdir}' exists")

    #Command exit
    elif cmd == 'exit':
        print("Sortie de Pyternet...\n")
        time.sleep(1)
        break
        language = ''

    #Erreur
    else:
        print(f"Oups... Nous n'avons pas trouvé la commande '{cmd}'. Réessayez !")
