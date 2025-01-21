from abc import ABC, abstractmethod
import math

class Forme(ABC):
    
    @abstractmethod
    def calculer_surface(self):
        pass

class Cercle(Forme):
    
    def __init__(self, rayon):
        self.rayon = rayon
    
    def calculer_surface(self):
        return math.pi * (self.rayon ** 2)

class Rectangle(Forme):
    
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def calculer_surface(self):
        return self.longueur * self.largeur


cercle = Cercle(8)
rectangle = Rectangle(2,7)

print("Surface du cercle:", cercle.calculer_surface())
print("Surface du rectangle:", rectangle.calculer_surface())
