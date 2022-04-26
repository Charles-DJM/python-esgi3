#Date : 28/03/2022
#Auteur : Charles de JAHAM
#Exercice 1 du TP1:

from inputFunc import inputChar, inputInt

def ex1():
    print("---Type prédéfinis---")
    print("Entrez un nombre entier : ")
    nombre = inputInt()
    print("Entrez un caractere : ")
    char = inputChar()
    print(f'{char} vaut {ord(char)}')
    print(f'{nombre} vaut {chr(nombre)}\n')