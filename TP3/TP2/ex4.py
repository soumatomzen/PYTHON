class Personne:

   def __init__(self,nom,prenom,age):

        self.nom=nom
        self.prenom=prenom
        self.age=age
    
   def se_presenter(self):
        print("je me présente : {self.nom} {self.prenom}, {self.age} ans.")
   
class Etudiant(Personne):
    def __init__(self, nom, prenom, age,matricule):
        super().__init__(nom, prenom,age)
        self.matricule=matricule
    def etudier(self):
        print("Je suis l'étudiant {self.prenom} {self.nom}, matricule {self.matricule}.")

P1=Personne("SOUMAYA","TOMZEN",23)
P2=Personne("SOUAD","CHOUIKHI",50)
E1=Etudiant("MOHAMED","TOMZEN",20,"123")
E2=Etudiant("SALMA","CHOUIKHI",20,"9999")


print("       " )
P1.se_presenter()
print("        ")
E1.etudier()
print("        ")
E2.se_presenter()
print("        ")
