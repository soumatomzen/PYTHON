class Comptebancaire:

    def __init__(self,titulaire,solde):
       
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self,montant):
        if montant>0:  
            self.solde+=montant
            print("le depot avec succès :",self.solde)
        else:
            print("le montant doit etre positif")
    
    def retirer(self,montant):
        if montant<=self.solde:
            self.solde-=montant
        else:
            print("le solde est insuffisant!!")
    
    def affichsolde(self):
        print("Votre solde est:",self.solde)
    
compte1=Comptebancaire("soumaya",60000)
compte2=Comptebancaire("souad",7000)

compte1.deposer(1400)
compte2.retirer(3000)       
compte1.affichsolde()
compte2.affichsolde()


