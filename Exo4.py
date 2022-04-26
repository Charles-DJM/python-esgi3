#Autheur: Charles de JAHAM
#Date: 24/04/2022
#Fichier de l'exercice 4

from inputFunc import inputPositiveInt
from util import generateTab

def ex4():
    print("---Factorielle---")
    print('Entrez un entier positif : ')
    number = inputPositiveInt()
    
    tab = generateTab(1,number+1)
    result = 1
    for i in range(len(tab)):
        result = result * tab[i]
    
    print(f'La factorielle de {number}, notée {number}!, et vaut :')
    printMultiplicationAscending(tab)
    print(f'= {result}')
    
    print(f'{result} = ', end="")
    printMultiplicationDescending(tab)    

#Ecris la multiplication des nombres dans le tableau dans l'ordre croissant
def printMultiplicationAscending(tab :list):
    for i in range(len(tab)):
        if(i == len(tab) - 1):
            print(f'{tab[i]} ', end="")
        else:
            print(f'{tab[i]} x ', end="")

#Ecris la multiplication des nombres dans le tableau dans l'ordre décroissant
def printMultiplicationDescending(tab :list):
    i = len(tab)
    while(i > 0):
        i = i - 1
        if(i == 0):
            print(f'{tab[i]} ', end="")
        else:
            print(f'{tab[i]} x ', end="")
