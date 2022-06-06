import os, time

def mkproj():
    project_name = input("Quel nom voulez-vous donner à votre projet ? > ")

    position = input("Voulez-vous créer votre projet dans un autre emplacement ? (y, n) > ")
    if position == "y" or "n":
        while True:
            if position == "y":
                    position = input("Entrez le chemin RELATIF de l'emplacement que vous voulez > ")
                    try:
                        os.chdir(position)
                        break
                    except:
                        print(f"FileNotFoundError: Dossier '{position}' n'existe pas/syntaxe invalide")

            elif position == "n" or "":
                pass
                break

            else:
                print(f"EntryError: Entrée '{position}' invalide !")
                break

    try:
        print(f"Nous créons votre projet avec le nom '{project_name}'...")
        os.mkdir(f"{project_name}")
        time.sleep(1)
        print("Votre projet a été créé avec succès !")
    except:
        print("Error: Une erreur est survenue !")

    open_project = input("Souhaitez-vous vous placer directement dans votre projet ? (y, n) > ")
    if open_project == "y":
        try:
            os.chdir(project_name)
            print(f"Le projet '{project_name}' est prêt à être utilisé !")
            ask_init = True
        except FileNotFoundError:
            print(f"FileNotFoundError: Projet '{project_name}' n'existe pas/syntaxe invalide.")
    elif open_project == "n" or "": print("Projet non-ouvert")

    else: print(f"EntryError: Entrée '{open_project}' introuvable.")

    if ask_init == True:
        init_project = input("Voulez-vous initialiser ce projet ? (y, n) > ")
        if init_project == "y":
            try:
                print("Création de 'index.html'...")
                html_file = open("index.html", "w")
                print("Création de 'style.css'...")
                css_file = open("style.css", "w")
                print("Terminé !")
            except:
                print("Error: Une erreur est survenue.")

        elif init_project == "n" or "": print("Projet non-initialisé.")

        else: print(f"EntryError: Entrée {init_project} introuvable.")
