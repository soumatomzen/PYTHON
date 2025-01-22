import json
etudiant={ 
    "etudiant":[
    {"nom":"ahmed","age":26 , "ville":"paris"},
    {"nom":"souma","age":23 , "ville":"pau"},
    {"nom":"sultan","age":18 , "ville":"caen"}
    ]
}

with open("c:\\Users\\LENOVO\\OneDrive\\Bureau\\etudiants.json", "w") as fichier:
     json.dump(etudiant, fichier, indent=4)
print("les informations bien enregistrées ")
with open("c:\\Users\\LENOVO\\OneDrive\\Bureau\\etudiants.json", "r") as fichier:
     lecture=json.load(fichier)
     print(lecture)