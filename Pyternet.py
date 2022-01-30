#Importation des modules
import os

import time

#Message de bienvenue
print("---------------------------- \n\
BIENVENUE SUR PYTERNET \n\
---------------------------- \n\
Pour avoir les instruction à suivre pour créer un projt, tapez \"instru\". \n\
Pour avoir la liste des commandes, tapez \"cmds\".")

#Fonctions des commandes
def cmds():
	print("---------------------------- \n\
VOICI LES COMMANDES \n\
---------------------------- \n\
		--- Création de projet --- \n\
 - instru : Avoir les instruction pour créer un projet. \n\n\
		--- Autres --- \n\
 - stop   : Stopper la création.")

def instru():
	print("---------------------------- \n\
VOICI LES INSTRUCTIONS \n\
---------------------------- \n\
Pour créer un projet Pyternet, tapez \"nproj\" \n\
Si vous avez déjà créé un projet Pyternet, vous pouvez passer aux commandes !")

def nproj():
	in_commande_func = input("Comment s'appelle votre projet ? ")

	projet_nom = in_commande_func

	print(f"Nous créons votre projet avec le nom \"{projet_nom}\"...")

	os.mkdir(f"{projet_nom}")

	time.sleep(1)

	print("Votre projet a été créé avec succès !")

#Boucle de détéction des commandes
while True:
	#Temps d'attente
	time.sleep(1)

	#Saut de ligne
	print()

	#Demande de commande
	in_commande = input("[Pyternet] > ")

	#Commande "cmds"
	if in_commande == 'cmds':
		cmds()

	#-- CREATION DE PROJET --

	#Commande "instru"
	elif in_commande == 'instru':
		instru()

	#Commande "nproj"
	elif in_commande == 'nproj':
		nproj()

	#-- AUTRES --
	elif in_commande == 'stop':
		break

	#Erreur
	else: 
		print(f"Oups... Nous n'avons pas trouvé la commande \"{in_commande}\". Réessayez !")
