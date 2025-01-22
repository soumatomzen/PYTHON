def safe_division(a,b):
    try:
        res=a/b
        print(res)
    except ZeroDivisionError:
        print("pas de division sur 0 ")
    else:
        
        print("division avec succés")

    finally :
       print("done")

a= int(input("saisir a:"))
b=int(input("saisir b:"))
res=safe_division(a,b)
print(res)