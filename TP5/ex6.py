import os
nom_actuel="phrases.txt"
nom_new="anciennes_phrases.txt"

try :
    os.rename(nom_actuel,nom_new)
    print("le fichier est renomé")
except FileNotFoundError:
    print("not exist")

    