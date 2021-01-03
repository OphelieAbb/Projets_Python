def afficher_information_personne(nom,age,taille=0):
    print()
    print("Vous vous appelez "+nom+", et vous avez "+str(age)+" ans .")
    print(f"Vous vous appelez {nom}, et vous avez {age}ans.")
    
    if  age >=18:
        print("Vous êtes majeur.")
    elif age ==17:
        print("Vous êtes presque majeur.")
    else:
        print("Vous êtes mineur  .")
    if taille != 0:
        print( "Votre taille : " + str(taille) + "m.")

        
def demander_nom():
    reponse_nom=""
    while reponse_nom == "":
        reponse_nom= input ("Entrez votre nom/prénom : ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input (nom_personne +"Entrez votre âge : ")
        try:
            age_int = int(age_str)
        except:
            print("Vous devez rentrer un chiffre.")
    return age_int

nom = demander_nom()
NB_PERSONNES = 4

for i in range (0,NB_PERSONNES):
    nom = "Individu " + str(i+1)
    age = demander_age(nom)
    afficher_information_personne(nom, age, 1.64 )
   



