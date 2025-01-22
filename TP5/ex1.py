with open('c:\\Users\\LENOVO\\OneDrive\\Bureau\\EXEMPLE.txt', 'r') as fichier:
    lignes = fichier.readlines()
    x = 1
    for ligne in lignes:
        print(x, ":", ligne.strip())  
        x += 1
