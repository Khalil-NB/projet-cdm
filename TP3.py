import random

#variables
niveau_vie = 20

force_adversaire = random.randint(2,10)

numero_adversaire = 0

numero_combat = 0

nombre_victoire = 0

nombre_defaites = 0

score_dés = random.randint(2,12)

nombre_victoires_consecutives = 0


#Choix de combat
while True:
    
    if nombre_victoire == 3:
        force_adversaire = 10

    print("Vous tombez face à face avec un adversaire de difficulté :",force_adversaire)
    Choix = int(input("Que voulez-vous faire ? \n\n 1- Combattre cet adversaire \n 2- Contourner cet adversaire et aller ouvrir une autre porte \n 3- Afficher les règles du jeu \n 4- Quitter la partie\n"))
    numero_adversaire += 1
    if Choix == 1:
        numero_combat += 1
        print("statut de la partie:","\n\nAdversaire:",numero_adversaire,"\nnombre de points de vie:",niveau_vie,"\nforce de l'aversaire:",force_adversaire,"\n\ncombat:",numero_combat)
        
#Victoire
        if score_dés > force_adversaire:
            nombre_victoire += 1
            print("vous obtenez:", score_dés,",Victoire!")
            print("vous avez ",niveau_vie,"points de vie restant","\n\n")
            nombre_victoires_consecutives += 1
            print("nombre de victoires consécutives:",nombre_victoires_consecutives)
            conteur_boss += 1
#Defaite            
        else:
            nombre_defaites += 1
            print("vous obtenez:", score_dés,", Défaite! \n")
            nombre_victoires_consecutives = 0
            niveau_vie -= force_adversaire
            print("vous avez ",niveau_vie,"points de vie restant","\n\n")
        
#conclusion/nombre de victoire et de défaites
        print(nombre_victoire,"victoires,",nombre_defaites,"défaites\n\n")
        force_adversaire = random.randint(2,10)    
    
#Contourner l'adversaire
    elif Choix == 2:
        print("Vous contournez l'adversaire (-1 point de vie)")
        niveau_vie -= 1
        print("vous avez ",niveau_vie,"points de vie restant","\n\n")
        force_adversaire = random.randint(2,10)
    
#Instruction du jeu        
    elif Choix == 3:
        print("Pour réussir un combat,il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.Dans ce cas,le niveau de vie de l’usager est augmenté par la force de l’adversaire.Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.Dans ce cas,le niveau de vie de l’usager est diminué par la force de l’adversaire.La partie se termine lorsque les points de vie de l’usager tombent sous 0.L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n\n")

#Quitter le programe
    elif Choix == 4:
        print("Merci et au revoir... ")
        quit()
#Erreur si le program recoit autre chose que 1-4        
    else:
        print("Une erreur c'est produit, veuillez entrer un nombre de 1-4 pour choisir une option")
    
#Si les points de vie vont en dessous de 0
    if niveau_vie < 1 :
        print("La partie est terminée, vous avez vaincu", nombre_victoire,"monstre(s).")
        
        niveau_vie = 20
        force_adversaire = random.randint(2,10)
        nombre_victoire = 0
        nombre_defaite = 0
        nombre_victoire_consecutives = 0
        numero_combat = 0
        numero_adversaire = 0
            
	

