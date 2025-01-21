class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom          
        self.__prenom = prenom     
        self.__age = age           

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        if isinstance(nom, str) and len(nom) > 0:
            self.__nom = nom
        else:
            raise ValueError("Le nom doit être une chaîne de caractères non vide.")

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, prenom):
        if isinstance(prenom, str) and len(prenom) > 0:
            self.__prenom = prenom
        else:
            raise ValueError("Le prénom doit être une chaîne de caractères non vide.")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            raise ValueError("L'âge doit être un entier supérieur ou égal 0.")


personne = Personne("soumaya", "tomzen", 23)
print("Nom:", personne.get_nom())
print("Prenom:", personne.get_prenom())
print("age:", personne.get_age())

personne.set_nom("Assia")
personne.set_prenom("Seh")
personne.set_age(21)

print("Nouveau nom:", personne.get_nom())
print("Nouveau prenom:", personne.get_prenom())
print("Nouvel age:", personne.get_age())
