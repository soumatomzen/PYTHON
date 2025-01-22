def read_file(filename):
    with open(filename,'r') as fichier:
        try:
           contenu = fichier.read()
           print(contenu)
        except FileNotFoundError :
           print("File not found")
        finally:
           if fichier:
               fichier.close()
               print('fermer')

file="c:\\Users\\LENOVO\\OneDrive\\Bureau\\exemple.txt"
res=read_file(file)
if res:
    print("contenu : ",res)

          