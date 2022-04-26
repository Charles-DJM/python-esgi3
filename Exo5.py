#Autheur: Charles de JAHAM
#Date: 24/04/2022

from inputFunc import inputPositiveInt

def ex5():
    print("---Table de multiplication---")
    print("Entrez un nombre entier positif")
    number = inputPositiveInt()
    print(f'Table de {number}:')
    for i in range(0, 11):
        print(f'- {number} x {i} = {number * i}')