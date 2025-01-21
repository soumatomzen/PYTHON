class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age 
    def getNom(self):
        return self.__nom
    def setNom(self,nom):
        self.__nom=nom
     def getPrenom(self):
        return self.__prenom
    def setPrenom(self,nom):
        self.__prenom=prenom
     def getage(self):
        return self.__age
    def setAge(self,age):
        self.__age=age