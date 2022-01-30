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
	print("""\n----------------------------
	VOICI LES COMMANDES
----------------------------
		\n--- Création de projet ---
 - instru : Avoir les instruction pour créer un projet.
		\n--- Autres ---
 - exit   : Quitter Pyternet.""")

def instru():
	print("""\n----------------------------
	VOICI LES INSTRUCTIONS
----------------------------
Pour créer un projet Pyternet, tapez 'new_project'
Si vous avez déjà créé un projet Pyternet, vous pouvez passer aux commandes !""")

def new_project():
	project_name = input("Quel nom voulez-vous donner à votre projet ? ")
	print(f"Nous créons votre projet avec le nom '{project_name}''...")
	os.mkdir(f"{project_name}")
	time.sleep(1)
	print("Votre projet a été créé avec succès !")


#Boucle de détéction des commandes
while True:
	#Temps d'attente
	time.sleep(1)
	#Demande de commande
	cmd = input("\n[Pyternet] > ")

	#Commande "cmds"
	if cmd == 'help':
		help()
	#-- CREATION DE PROJET --
	#Commande "instru"
	elif cmd == 'instru':
			instru()
	#Commande "new_project"
	elif cmd == 'new_project':
			new_project()

	#-- AUTRES --
	#Quitter la Boucle
	elif cmd == 'exit':
			break

	#Erreur
	else:
		print(f"Oups... Nous n'avons pas trouvé la commande '{cmd}'. Réessayez !")
