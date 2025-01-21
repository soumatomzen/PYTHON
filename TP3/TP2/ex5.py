class Animal:
    def faire_du_bruit(self):
        raise NotImplementedError("Cette méthode doit être implémentée dans une sous-classe.")
class Chien(Animal):
    def faire_du_bruit(self):
        return "HOWHOW!"

class Chat(Animal):
    def faire_du_bruit(self):
        return "Miao!!"

def tester_animaux():
    animaux = [Chien(), Chat()]
    for Animal in animaux:
        print(f"{Animal.__class__.__name__} fait : {Animal.faire_du_bruit()}")

tester_animaux()
