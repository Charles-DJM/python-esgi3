#Date : 28/03/2022
#Auteur : Charles de JAHAM
from inputFunc import inputFloat

def calculTrapeze(a : float, b : float, c : float):
    return (a + b) * c * 0.5

def ex2():
    print("---Calcul d'une surface---")
    print('Entrez A : ')
    a = inputFloat()
    print('Entrez B : ')
    b = inputFloat()
    print('Entrez C : ')
    c = inputFloat()
    
    print(f'La surface du trapeze est {calculTrapeze(a,b,c)}')