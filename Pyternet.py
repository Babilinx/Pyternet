#Importation des modules
import os
import time

#Message de bienvenue
print("""----------------------------
BIENVENUE SUR PYTERNET
----------------------------
Pour avoir les instruction à suivre pour créer un projet, tapez 'instru'.
Pour avoir la liste des commandes, tapez 'help'.""")


#Fonctions des commandes
def help():
	print("""\n--------------------------------------------------------
	VOICI LES COMMANDES
--------------------------------------------------------
		\n--- Création de projet ---
 - instru : Avoir les instruction pour créer un projet.
 - mkproj : Création d'un projet.
 - init   : initialiser la création d'un projet (effectuer dans le dossier projet).
 		\n--- Ouvrir un projet ---
 - open   : Ouvrir un projet déjà existant
		\n--- Autres ---
 - cd     : Changer de répertoire.
 - mkdir  : Créer un dossier.
 - exit   : Quitter Pyternet.""")

def instru():
	print("""\n--------------------------------------------------------
	VOICI LES INSTRUCTIONS
--------------------------------------------------------
Pour créer un projet Pyternet, tapez 'new_project'
Si vous avez déjà créé un projet Pyternet, ouvrez-le avec 'open' !""")

def mkproj():
	project_name = input(f"Quel nom voulez-vous donner à votre projet ? \n[Pyternet/{dir}:create] > ")
	print(f"Nous créons votre projet avec le nom '{project_name}'...")
	os.mkdir(f"{project_name}")
	time.sleep(1)
	print("Votre projet a été créé avec succès !")

def open_project(project_name):
	#On regarde si le nom du projet existe
	try:
		os.chdir(project_name)
		print(f"Projet {project_name} prêt à être utilisé !")
	except FileNotFoundError:
		print(f"FileNotFoundError: Dossier '{project_name}' n'existe pas/syntaxe invalide")
		pass

def init():
	print("Création de 'index.html'...")
	html_file = open("index.html", "w")
	print("Création de 'style.css'...")
	css_file = open("style.css", "w")
	print("Terminé !")

dir = ""
#Boucle de détection des commandes
while True:
	#Temps d'attente
	time.sleep(1)
	#Demande de commande
	cmd = input(f"\n[Pyternet{dir}] > ")

	#Commande "cmds"
	if cmd == 'help':
		help()
	#-- CREATION DE PROJET --
	#Commande "instru"
	elif cmd == 'instru':
		instru()
	#Commande "new_project"
	elif cmd == 'mkproj':
		mkproj()
	#commende pour ouvrir un projet
	elif cmd == "open":
		project_name = input("Nom du projet à ouvrir\n[Pyternet:open] > ")
		open_project(project_name)
		dir = f"/{project_name}"
	#commende pour initialiser un projet
	elif cmd == "init":
		init()

	#-- AUTRES --
	#Se déplacer
	elif cmd == "cd":
		chdir = input(f"\n[Pyternet{dir}:cd] > ")
		try:
			os.chdir(chdir)
			dir += f"/{chdir}"
		except FileNotFoundError:
			print(f"Error: {chdir} do not exists.")
			pass
	#Créer un nouveau Dossier
	elif cmd == "mkdir":
		mkdir = input(f"\n[Pyternet{dir}:mkdir] > ")
		try: os.mkdir(mkdir)
		except FileExistsError:
			print(f"Error: '{mkdir}' exists")
			pass
	#Quitter la Boucle
	elif cmd == 'exit':
		break

	#Erreur
	else:
		print(f"Oups... Nous n'avons pas trouvé la commande '{cmd}'. Réessayez !")
