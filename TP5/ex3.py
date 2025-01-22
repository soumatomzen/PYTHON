A = input("voulez-vous ajouter des phrases ?").strip().lower()
while A=="oui":
    with open ("c:\\Users\\LENOVO\\OneDrive\\Bureau\\phrases.txt","a")as fiichier:
        phrase=str(input('ajouter cette phrase : \n'))
        fiichier.write(phrase + "\n")
        A = input("voulez-vous ajouter des phrases ? ").strip().lower()
print("bien enregistré.")