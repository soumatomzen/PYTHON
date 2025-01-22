def process_input(user_input):
    try :
        user=int(user_input)
        res=10/user
        print(res)
    except ValueError :
        print("pas de convertissement")
    except ZeroDivisionError :
        print("interdire la division sur 0")
        
        
try:
    a =input("saisir un nombre")
    process_input(a)
except ValueError as e:
    print(e)
except ZeroDivisionError as z:
    print(z)
    
