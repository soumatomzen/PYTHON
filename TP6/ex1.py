def safe_division(a,b):
    if b==0 :
        raise ZeroDivisionError("impossible la division sur 0 ")
    return a/b

a= int(input("saisir a:"))
b=int(input("saisir b:"))
res=safe_division(a,b)
print(res)