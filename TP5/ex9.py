def statistique(fichier):
    try:
        with open(fichier, "r") as file:
            contenu = file.readlines()
        nmbr_lignes = len(contenu)
        nmbr_mots = 0
        nmbr_caracteres = 0

        for ligne in contenu:
            nmbr_mots += len(ligne.split()) 
            nmbr_caracteres += len(ligne)   

        print(f"Statistiques de'{fichier}':")
        print(f"Nombre total de lignes : {nmbr_lignes}")
        print(f"Nombre total de mots : {nmbr_mots}")
        print(f"Nombre total de caractères : {nmbr_caracteres}")

    except FileNotFoundError:
        print(f"Le fichier '{fichier}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


nom_fichier = "journal.txt" 
statistique(nom_fichier)
