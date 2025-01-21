
def somme_varargs(*args):
    somme = 0
    for nombre in args:
        somme += nombre
    return somme

print(somme_varargs(1, 2, 3, 4))