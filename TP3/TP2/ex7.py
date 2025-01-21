class livre:

    def __init__(self,titre,auteur,annee_publication):
        self.titre=titre
        self.auteur=auteur
        self.annee_publication=annee_publication
    
class bibliotheque:
    def __init__(self):  
        self.livres = []
    def ajouter_livre(self,livre):
        self.livres.append(livre)
        print("le livre ' {livre } ' est ajouté")

    def afficher_livres(self):
        if not self.livres:
            print("la bibliothèque est vide")
        else:
            print("les livres:'{self.livres}'")
    

livre1 = livre("La boite à merveille","sefrioui",1998)
bibliotheque = bibliotheque()
bibliotheque.ajouter_livre("La boite à merveille")
bibliotheque.afficher_livres()
