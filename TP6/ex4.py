class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age<0:
        raise NegativeAgeError("l'age est négative")
    return age

try :
    age=set_age(9)
    print(age)
except NegativeAgeError as e:
    print(e)