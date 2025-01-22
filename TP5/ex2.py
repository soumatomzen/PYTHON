with open("c:\\Users\\LENOVO\\OneDrive\\Bureau\\phrases.txt","w") as fichier:
    for i in range(0,3):
        phrase=str(input('entrer une phrase \n'))
        fichier.write(phrase + "\n")
with open ("c:\\Users\\LENOVO\\OneDrive\\Bureau\\phrases.txt","a")as fiichier:
    phrase=str(input('ajouter cette phrase: \n'))
    fiichier.write(phrase)