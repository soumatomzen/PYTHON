class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom       
        self.__prix = prix     

    def get_nom(self):
        return self.__nom

    def get_prix(self):
        return self.__prix

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit   
        self.quantite = quantite 

    def get_cout_total(self):
        return self.produit.get_prix() * self.quantite

class Panier:
    def __init__(self):
        self.commandes = [] 

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        total = 0
        for commande in self.commandes:
            total += commande.get_cout_total()
        return total


produit1 = Produit("robe", 300)
produit2 = Produit("chemise",250)

commande1 = Commande(produit1, 1)
commande2 = Commande(produit2, 2)

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

print(f"Total du panier: {panier.calculer_total()} Dh")
