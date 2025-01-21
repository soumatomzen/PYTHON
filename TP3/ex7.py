from abc import ABC, abstractmethod

class Vehicule(ABC):
    
    @abstractmethod
    def deplacer(self):
        pass

class Voiture(Vehicule):
    
    def __init__(self, marque):
        self.marque = marque
    
    def deplacer(self):
        return f'La voiture {self.marque} roule.'

class Bicyclette(Vehicule):
    
    def __init__(self, type_bicyclette):
        self.type_bicyclette = type_bicyclette
    
    def deplacer(self):
        return f'La bicyclette {self.type_bicyclette} pédale.'


voiture = Voiture("kia")
bicyclette = Bicyclette("x")

print(voiture.deplacer())
print(bicyclette.deplacer())