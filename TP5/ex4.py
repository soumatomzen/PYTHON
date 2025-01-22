import csv
donnee=[
    ["Nom","Age","ville"],
    ["soumaya",23,"tantan"],
    ["aya",22,"dakhla"],
    ["assia",23,"safi"]   
]
with open("c:\\Users\\LENOVO\\OneDrive\\Bureau\\contacts.csv",mode='w',newline='')as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerows(donnee)
       