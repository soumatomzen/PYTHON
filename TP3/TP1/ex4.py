def cpt_occurence(liste):
    dic={}
    for i in liste:
        a=liste.count(i)
        dic[i]=a
    return dic
liste=['ROUGE','BLEU','ORANGE','BLANC','NOIR']
print(cpt_occurence(liste))

