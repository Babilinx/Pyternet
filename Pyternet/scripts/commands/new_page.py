import os, time

def new_page(page_name, title):
    file = open(f"{page_name}", "w")

    print("Création de la page effectuée.")

    time.sleep(1)

    print("Initialisation de la page...")

    file.write(f"""<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"utf-8\">
        <title>{title}</title>
    </head>

    <body>

    </body>
</html>""")

    file.close()

    time.sleep(1)

    print("Initialisation effectuée !")
