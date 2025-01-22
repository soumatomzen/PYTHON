def read_file_and_get_integer():
    while True:
        try:
            file_name = input("entrer le nom du fichier: ")
            with open(file_name, 'r') as file:
                content = file.read()
            print("\nContenu du fichier :")
            print(content)
            break
        except FileNotFoundError:
            print("Erreur : Le fichier n'existe pas.")
        except Exception as e:
            print("Erreur")

    while True:
        try:
            user_input = input("entrer un entier : ")
            nombre = int(user_input) 
            print("Vous avez entré l'entier :")
            return file_name, nombre
        except ValueError:
            print("Erreur")
read_file_and_get_integer()
