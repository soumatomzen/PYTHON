def get_positive_integer():
    while True:
        try:
            user_input = input("entrer un entier positif : ")
            nombre = int(user_input)
            if nombre <= 0: 
                raise ValueError("Le nombre doit être positif.")
            return nombre
        except ValueError as e:
            print(e)
