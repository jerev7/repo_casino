#-*-coding: utf-8 -*

from random import randrange
from math import ceil




argent_joueur = 300
print("Vous disposez de", argent_joueur, " euros")

somme_mise = input("choisissez la somme que vous souhaitez miser : \n")
somme_mise = int(somme_mise)
	
chiffre_choisi = input("choisissez le chiffre sur lequel vous souhaitez miser : \n")
chiffre_choisi = int(chiffre_choisi)
random_nbr = randrange(50)
print("La roulette est tombée sur : ", random_nbr)

if chiffre_choisi % 2 == 0 and random_nbr % 2 == 0:
	gain = 50 * somme_mise / 100
elif chiffre_choisi % 2 != 0 and random_nbr % 2 != 0:
	gain = 50 * somme_mise / 100
elif chiffre_choisi == random_nbr:
	gain = 3 * somme_mise
else: 
	gain = 0
print("votre gain est de : ", gain)
argent_joueur = 300 - somme_mise + ceil(gain)
print("vous disposez désormais de : ", argent_joueur, " euros !")







"""
roulettre : nombre aléatoire entre 0 et 50 avec randrange
			si multiple de deux = noir, sinon rouge


resultat =  si les 2 numeros sont les mêmes : gain = 3*Somme misée
			si les 2 numeros sont pairs ou les 2 numeros sont impairs : gain = 50*Somme misée / 100
			sinon : gain = 0

nouvelle valeur de l'argent du joueur(arrondie par la fonction ceil) = argent de base - somme misée + résultat

Tant que argent du joueur > 0, relancer la mise et la roulette
"""





