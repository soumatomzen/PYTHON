class Voiture:

    def __init__(self, marque,modele,annee):
       
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print("la marque de voiture est:",self.marque)
        print("le modele de voiture est:",self.modele)
        print("l'annee de voiture est:",self.annee)


Voi1=Voiture("dacia","sandero",2008)
Voi2=Voiture("renaut","laguna",2005)
Voi3=Voiture("audi","q5",2018)


Voi1.afficher_info()
print("      ")
Voi2.afficher_info()
print("      ")
Voi3.afficher_info()

