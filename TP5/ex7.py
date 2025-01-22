import os
import shutil

base_path = "C:\\Users\\LENOVO\\OneDrive\\Bureau\\TP\\TP5"

journal_path = os.path.join(base_path, "journal.txt")
with open(journal_path, "w") as file:
    file.write("soumaya tomzen\n")
    file.write("ma ville natale est tantan\n")
    file.write("étudiante en iise\n")
print("création avec succès")


copie_path = os.path.join(base_path, "journal_copie.txt")
shutil.copy(journal_path, copie_path)
print("Le fichier est copié")


archives_path = os.path.join(base_path, "archives")
if not os.path.exists(archives_path):
    os.mkdir(archives_path)

shutil.move(copie_path, os.path.join(archives_path, "journal_copie.txt"))
print("Le fichier est déplacé dans le dossier archives")
