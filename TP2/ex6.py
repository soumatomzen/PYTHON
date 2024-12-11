class Rectangle:
    
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
    
    def calculer_surface(self):
        surface=self.largeur*self.hauteur
        print("la surface est :",surface)
    
    def calculer_perimetre(self):
        perimetre=self.largeur+self.hauteur
        print("le perimetre est :",perimetre)
    
rect1=Rectangle(9,3)
rect2=Rectangle(13,11)

rect1.calculer_perimetre()
rect2.calculer_surface()
    