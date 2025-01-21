class Vehicule:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def afficher_info(self):
        return '{} {} {}'.format(self.marque,self.modele,self.annee)
v1=Vehicule("KIA","SPORTAGE",2012)
v1.afficher_info()


class Moteur:
     def __init__(self,puissance,type_moteur):
         if type_moteur not in ["essence","disel","électrique"]:
            raise ValueError("Le moteur doit etre de type 'Essence'.")
         self.puissance = puissance
         self.type_moteur = type_moteur
     def afficher_moteur(self):
         return '{} {}'.format(self.puissance,self.type_moteur)
M1=Moteur(8,"essence")         
M1.afficher_moteur() 


class Voiture(Vehicule,Moteur):
     def __init__(self,marque,modele,annee,puissance,type_moteur,nombre_de_places):
         Vehicule.__init__(self,marque,modele,annee)
         Moteur.__init__(self,puissance,type_moteur)
         self.nombre_de_places=nombre_de_places
     def afficher_info(self):
         return '{} {} {}'.format(Vehicule.afficher_info(self),Moteur.afficher_moteur(self),self.nombre_de_places)
VOITU=Voiture("KIA","SPORTAGE",2012,8,"essence",4) 
VOITU.afficher_info()

class Moto(Vehicule,Moteur):
     def __init__(self,marque,modele,annee,puissance,type_moteur,type_moto):
         Vehicule.__init__(self,marque,modele,annee)
         Moteur.__init__(self,puissance,type_moteur)
         self.type_moto=type_moto
     def afficher_info(self):
         return '{} {} {}'.format(Vehicule.afficher_info(self),Moteur.afficher_moteur(self),self.type_moto)
Moto1=Moto("TMAX","TM",2000,7,"essence","sport") 
Moto1.afficher_info()