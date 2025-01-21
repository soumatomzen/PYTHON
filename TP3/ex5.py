class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom         
        self.prenom = prenom   
        self.salaire = salaire 

    def afficher(self):
        return f'Nom: {self.nom}, Prénom: {self.prenom}, Salaire: {self.salaire}'

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire) 
        self.employes_sous_supervision = []    

    def ajouter(self, employe):
        self.employes_sous_supervision.append(employe)

    def afficher_supervises(self):
        for employe in self.employes_sous_supervision:
            print(employe.afficher())


employe1 = Employe("saadia", "chouikhi", 16500)
employe2 = Employe("mohmed", "tomzen", 8700)
manager = Manager("souma", "tmz", 2500)
manager.ajouter(employe1)
manager.ajouter(employe2)

print("Informatuin du manager :")
print(manager.afficher())

print("Les employés supervisés par le manager :")
manager.afficher_supervises()
