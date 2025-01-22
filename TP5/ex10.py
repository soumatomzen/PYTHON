import csv

fichier_csv = "contacts.csv"
def afficher():
    print("\n1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Rechercher un contact")
    print("4. Supprimer un contact")
    
def ajouter():
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    telephone = input("Tél: ")
    email = input("Email: ")
    with open(fichier_csv, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nom,prenom,telephone, email])

def afficher_contacts():
    try:
        with open(fichier_csv, "r") as file:
            reader = csv.reader(file)
            for contact in reader:
                print(", ".join(contact))
    except FileNotFoundError:
        print("Le fichier n'existe pas.")

def rechercher():
    recherche = input("Entrez le nom: ")
    try:
        with open(fichier_csv, "r") as file:
            reader = csv.reader(file)
            for contact in reader:
                if contact[0].lower() == recherche.lower():
                    print(", ".join(contact))
                    return
            print("Contact n'existe pas.")
    except FileNotFoundError:
        print("Le fichier n'existe pas.")

def supprimer():
    recherche = input("Entrez le nom: ")
    lignes = []
    try:
        with open(fichier_csv, "r") as file:
            reader = csv.reader(file)
            lignes = list(reader)
        with open(fichier_csv, "w", newline="") as file:
            writer = csv.writer(file)
            for contact in lignes:
                if contact[0].lower() != recherche.lower():
                    writer.writerow(contact)
        print("Contact bien supprimé.")
    except FileNotFoundError:
        print("Le fichier n'existe pas.")

def main():
    while True:
        afficher()
        choix = input("Choisir une option: ")
        if choix == "1":
            ajouter()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher()
        elif choix == "4":
            supprimer()
        else:
            print("Choix invalide.")
if __name__ == "__main__":
    main()
