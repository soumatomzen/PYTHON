class Personne:
   def __init__(self,prenom): 
      self.prenom = prenom
      self.amis=[]
    
   def ajouter_amis(self,ami):
      self.amis.append(ami)
      print("'{ami.prenom}' est ajouté au liste des amis de '{self.prenom}' ")
 
   def afficher_amis(self):
      if not self.amis:
         print("liste est vide")
      else:
       print(f"Liste des amis de '{self.prenom}' :")
      for index, ami in enumerate(self.amis, start=1):
       print(f"{index}. {ami.prenom}")


p1=Personne("assia")
p2=Personne("basma")
p3=Personne("aya")
p4=Personne("houda")

p1.ajouter_amis(p2)
p3.ajouter_amis(p4)
p1.afficher_amis()
p2.afficher_amis()
p3.afficher_amis()