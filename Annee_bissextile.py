annee = input("Saisissez une année :")
try:
    annee = int(annee) # Conversion de l'année
    if annee<=0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")

if annee % 4 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = True
elif annee % 400 == 0:
    bissextile = True
else :
    bissextile = False

if bissextile :
    print("L'année est bissextile!")
else:
    print("L'année n'est pas bissextile.")
    
