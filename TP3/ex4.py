class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom       
        self.__prix = prix     

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        if isinstance(nom, str) and len(nom) > 0:
            self.__nom = nom
        else:
            raise ValueError("Le nom doit être une chaîne de caractères non vide.")

    def get_prix(self):
        return self.__prix

    def set_prix(self, prix):
        if isinstance(prix, (int, float)) and prix >= 0:
            self.__prix = prix
        else:
            raise ValueError("Le prix doit être un nombre supérieur ou égal 0.")

    def calculer_remise(self, remise, seuil_remise):
        if self.__prix > seuil_remise:
            return self.__prix * (1 - remise / 100)
        else:
            return self.__prix


produit = Produit("robe", 300)
print("produit:", produit.get_nom())
print("Prix sans remise:", produit.get_prix())
prix_avec_remise = produit.calculer_remise(25, 500)
print("Prix avec remise:", prix_avec_remise)
