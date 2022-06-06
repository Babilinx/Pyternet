def set_title(page_name : str, text : str):
    # Set the page's  title
    try:
        file = open(page_name, 'w')
        file.write(f"""<!DOCTYPE html>
            
<html>
    <head>
        <meta charset=\"utf-8\">
        <title>{text}</title>
    </head>
    <body>\n""")
    except FileNotFoundError:
        pass

def config_page(page_name : str = None):
    try:
        file = open(page_name, 'w')
        file.close()
        continuer = True
    except FileNotFoundError:
        print(f"FileNotFoundError: Page '{page_name}' n'existe pas/syntaxe invalide")
        
    if continuer:
        page_title = input("Quel est le nouveau titre de la page ? > ")
        set_title(f"{page_name}", f"{page_title}")
        
        while True:
            instruction = input("""Tapez une instruction :
            
 p : Ajouter du texte.
 h1 : Ajouter un titre de niveau 1.
 br : Mettre un espace.
 stop : Stopper.
 
 > """)
            if instruction == "p" or "h1" or "br" or "stop":
                if instruction == "p":
                    inpt = input("Entrez le texte. > ")
                    file = open(page_name, 'a')
                    file.write(f"<p>{inpt}</p>\n")
                    file.close()
                elif instruction == "h1":
                    inpt = input("Entrez le texte. > ")
                    file = open(page_name, 'a')
                    file.write(f"<h1>{inpt}</h1>\n")
                    file.close()
                elif instruction == "br":
                    file = open(page_name, 'a')
                    file.write("<br>\n")
                    file.close()
                elif instruction == "stop":
                    print("Sortie en cours...")
                    break
                else: 
                    print(f"CommandError: Command {instruction} not found!")    
            else: 
                print(f"CommandError: Command {instruction} not found!")