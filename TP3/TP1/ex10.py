def fusionner_dicts(dict1, dict2):
    fusionne = dict1.copy()
    for cle, valeur in dict2.items():
        if cle in fusionne:
            fusionne[cle] += valeur
        else:
            fusionne[cle] = valeur

    return fusionne

dict1 = {'a': 99, 'b': 88, 'c': 77}
dict2 = {'b':44, 'c': 55, 'd': 66}
resultat = fusionner_dicts(dict1, dict2)
print(resultat)