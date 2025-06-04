

def my_cal():
    a = int(input("saisi une valeur pour a"))
    b = int(input("saisi une valeur pour b"))
    somme = a+b
    print(f"{a} + {b} = ", somme)
    soustration = a-b
    print(f"{a} - {b} = ", soustration)
    multiplication = a*b
    print(f"{a} * {b} = ", multiplication)
    if b != 0 : 
        division =a/b 
    else :
        print("ERREUR, veillez entrez une valeur correcte svp")
    print(f"{a} / {b} = ", division)

my_cal() 


     