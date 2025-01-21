class Moteur:
     def __init__(self,puissance,type_moteur):
         if type_moteur not in ["essence","disel","électrique"]:
            raise ValueError("Le moteur ne peut être créé que si le type est 'Essence'.")
         self.puissance = puissance
         self.type_moteur = type_moteur
     def afficher_moteur(self):
         return '{} {}'.format(self.puissance,self.type_moteur)
M1=Moteur(4,"essence")         
M1.afficher_moteur()         