#Date : 28/03/2022
#Auteur : Charles de JAHAM
#Fichier de l'exercice 3

from inputFunc import inputPositiveInt
from util import generateTab

#Ecrit la somme des nombres dans tab dans l'ordre décroissant
def printDescending(tab : list):
    print(f'{sum(tab)} = ', end="")    
    i = len(tab)
    while(i > 0):
        i = i - 1
        if(i == 0):
            print(f'{tab[i]} ', end="")
        else:
            print(f'{tab[i]} + ', end="")
            
#Ecrit la somme des nombres dans tab dans l'ordre croissant
def printAscending(tab : list):
    for i in tab:
        if(i == len(tab) - 1):
            print(f'{tab[i]} ', end="")
        else:
            print(f'{tab[i]} + ', end="")
    print(f'= {sum(tab)}')

def ex3():
    print('---Somme---')
    print('Entrez un entier positif : ')
    number = inputPositiveInt()
    tab = generateTab(0, number+1)
    printAscending(tab)
    printDescending(tab)