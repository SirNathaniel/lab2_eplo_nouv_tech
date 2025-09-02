import random
import string

def jouer_nombre():
    n = random.randrange(1, 100)
    guess = int(input("Entrez un nombre entre 1 et 100 : "))
    
    while guess != n:
        if guess < n:
            print("Trop bas !")
        elif guess > n:
            print("Trop haut !")
        guess = int(input("Essayez encore : "))
    
    print("Bravo, vous avez deviné le bon nombre !")


def jouer_lettre():
    lettre = random.choice(string.ascii_lowercase)  # une lettre de a à z
    guess = input("Entrez une lettre (a-z) : ").lower()
    
    while guess != lettre:
        if guess < lettre:
            print("La lettre mystère est plus loin dans l'alphabet.")
        elif guess > lettre:
            print("La lettre mystère est plus tôt dans l'alphabet.")
        guess = input("Essayez encore : ").lower()
    
    print("Bravo, vous avez deviné la bonne lettre !")


def menu():
    while True:
        print("\n=== JEU DU MYSTÈRE ===")
        print("1. Deviner un nombre")
        print("2. Deviner une lettre")
        print("3. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            jouer_nombre()
        elif choix == "2":
            jouer_lettre()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez entrer 1, 2 ou 3.")

        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != "o":
            print("Merci d'avoir joué ! À bientôt.")
            break


# Lancer le jeu
menu()
