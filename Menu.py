#Date: 28/03/2022
#Auteur: Charles de JAHAM
#Ce fichier est le fichier à lancer pour executer le programme

from Exo1 import ex1
from Exo2 import ex2
from Exo3 import ex3
from Exo4 import ex4
from Exo5 import ex5
from Exo6 import ex6
from Exo7 import ex7
from Exo8 import ex8

def getChoice():
    print("\n")
    while True:    
        try:
            choix = int(input('Quel exercice voulez vous faire ?\n1- Types prédéfinis \n2- Calcul d’une surface \n3 -Somme \n4- factorielle \n5- Table multiplication \n6- Saisie de nombres et de caractères\n7- Calcul de crédit\n8- Le plus grand \n9- Quitter\n>'))
            if(choix < 0 or choix > 10):
                raise Exception('Entrez un choix valide !\n')            
        except ValueError:
            print('Entrez un nombre entier !\n')
        except Exception as e:
            print(e)
        else:
            return choix
            
def main():
    while True:
        choice = getChoice()
        if(choice == 1):
            ex1()
        elif(choice == 2):
            ex2()
        elif(choice == 3):
            ex3()
        elif(choice == 4):
            ex4()
        elif(choice == 5):
            ex5()
        elif(choice == 6):
            ex6()
        elif(choice == 7):
            ex7()
        elif(choice == 8):
            ex8()
        elif(choice == 9):
            return
main()