class Vehicule:
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def afficher_info(self):
        return '{} {} {}'.format(self.marque,self.modele,self.annee)
v1=Vehicule("X","Y",2004)
v1.afficher_info()