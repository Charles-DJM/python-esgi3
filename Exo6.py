#Autheur: Charles de JAHAM
#Date: 24/04/2022
#Fichier de l'exercice 6

from math import log, sin, cos
from inputFunc import inputPositiveInt

def ex6():
    print("---Saisie de nombres et de caratères---")
    print("Entrez un nombre entier")
    number = inputPositiveInt()
    
    print(f'ln({number}) = {log(number)}')
    print(f'sin({number}) = {sin(number)}')
    print(f'cos({number}) = {cos(number)}')