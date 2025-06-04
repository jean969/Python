import random
def devinette():
    print("Bienvenu dans mon de devinette!")
    print("Je pense à un nombre entre 1 et 10,quel est ce nombre ? ")
    nombre_secret= random.randint(1,10)
    tempative = 0
    while True :
        try: 
            user = int(input("Entrez votre supposition...."))
            tempative += 1
            if user < 1 or user > 10 :
                print("Viellez entrer un nombre entre 1 et 10")
        
            elif user < nombre_secret :
                print("Trop bas, essayez encore ")
            elif user > nombre_secret :
                print("Trop grand, essayez encore")
            else : 
                print("Bravo vous avez gagné")
            break
        except ValueError :
            print("Valeur invalide. Viellez saisir un nombre entier ")
devinette()    