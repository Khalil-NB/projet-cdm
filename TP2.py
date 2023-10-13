#Par Khalil Nait Bahloul
#13 octobre 2023

#trouve le nombre

import random
import os
from os.path import exists
import shelve
import sys
import subprocess

#variable
nombreEssais=0
inconnu=random.randint(1,1000)
essai=0
print(inconnu)

#definir verifie_essai
def verifie_essai() :
    if essai > inconnu :
      print("\nL'inconnu est plus petit ")
      
    elif essai < inconnu :
      print("\nL'inconnu est plus grand ")

#Jeu     
while (essai != inconnu) :
    essai = int(input("Entrez un chiffre de 0 à 1000 \n:"))
    nombreEssais += 1
    verifie_essai()
    
    #mauvaise réponse
    if essai != inconnu :
        print("Mauvaise réponse, vous avez essayé : %d fois sans réussir \n"%nombreEssais)
        
    #bonne réponse/score   
    elif essai == inconnu:
        print("\n\nBravo bonne réponse! Votre nombre d'éssais est : %d "%nombreEssais)
        
#recommencer?
    recommencer=str(input(print("Voulez-vous relancer une nouvelle partie?\n")))

    if recommencer == "oui":
       inconnu = random.randint(1,1000)
      
    else:
        exit()        

      
