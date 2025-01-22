try:
    
    with open("inexistant.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    
    print("Le fichier n'existe pas.")
except Exception as e:
    
    print(f"Une erreur s'est produite : {e}")
