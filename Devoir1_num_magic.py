import random

Recommencer = True

while(Recommencer):
    a=random.randint(0,500)
    for i in range (1,6):
        print(f"il vous reste:{6-i} chance")
        
        user_number = input("=====TROUVER LE BON NOMBRE====== \n")
        
        user_number=int(user_number)

        if user_number > a:
            print("le chiffre est trop grand \n Reessayez")
            
        elif user_number < a : 
            print("le chiffre est trop petit \n Ressayez")
        else: 
            print("*******VOUS AVEZ GAGNE******")
            break
    print("Le nombre etait:")
    print(a)

    print("voulez-vous rejouer?")
    answer= input("Votre reponse: ")
    if answer == "oui" :
        Recommencer=True
    else :
        Recommencer=False

