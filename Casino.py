from random import randrange
import os
import math

argent = 1000
continuer_partie = True

print("Vous vous installez à la table de roulette avec", argent, "€.")

while continuer_partie:
    
    nombre_mise = -1
        
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Choisir une nombre sur lequel miser (entre 0 et 49):")
        nombre_mise = int(nombre_mise)
        
    mise = 0

    while mise <= 0 or mise > argent:
        mise = input( "Tapez le montant de votre mise : ")
        mise = int(mise)
        
    numero_gagnant = randrange(50)

    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

    if numero_gagnant == nombre_mise :
        print("Bravo tu as gagné ! tu obtiens la somme de :", mise*3,"€.")
        argent += mise
    else :
        print("Tu as perdu ! ")
        argent -= mise
    
    if argent < 0:
        print("Tu n'as plus d'argent")
        continuer_partie = False
    else:
        print("Vous avez à présent", argent, "€.")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")

    if quitter == "o" or quitter == "O":
        print("Vous quittez le casino avec vos gains.")
        continuer_partie = False



