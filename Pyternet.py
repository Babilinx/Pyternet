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
 - exit   : Quitter Pyternet.""")

def instru():
	print("""\n--------------------------------------------------------
	VOICI LES INSTRUCTIONS
--------------------------------------------------------
Pour créer un projet Pyternet, tapez 'mkproj'
Si vous avez déjà créé un projet Pyternet, ouvrez-le avec 'open' !""")

def mkproj():
	project_name = input("Quel nom voulez-vous donner à votre projet ? \n[Pyternet/create] > ")
	print(f"Nous créons votre projet avec le nom '{project_name}''...")
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
	html_file = open("index.html", "w")
	css_file = open("style.css", "w")

dir = ""
#Boucle de détection des commandes
while True:
	#Temps d'attente
	time.sleep(1)
	#Demande de commande
	cmd = input(f"\n[Pyternet/{dir}] > ")

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
		dir = project_name
	#commende pour initialiser un projet
	elif cmd == "init":
		init()

	#-- AUTRES --
	#Quitter la Boucle
	elif cmd == 'exit':
		break

	#Erreur
	else:
		print(f"Oups... Nous n'avons pas trouvé la commande '{cmd}'. Réessayez !")
