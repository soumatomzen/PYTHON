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

def afficher_surface(formes):
    for forme in formes:
        print(f'Surface est {forme.calculer_surface()}')

cercle = Cercle(2)
rectangle = Rectangle(8,9)
formes = [cercle, rectangle]
afficher_surface(formes)
