def convert_to_int(value):
    try :
       return int(value)
    except ValueError :
       raise ValueError("impossiible de convertiir en un entier")
try:
   a= input("saisir une valeur :") 
   res=convert_to_int(a)
   print(res)
except ValueError as e:
    print(e)