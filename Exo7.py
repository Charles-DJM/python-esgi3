#Autheur: Charles de JAHAM
#Date: 24/04/2022
#Fichier de l'exercice 7

from inputFunc import inputFloat, inputPositiveInt


def ex7():
    print("---Calcul de crédit---")
    print("Entrez le motant du capital emprunté:")
    montant = inputFloat()
    print("Nombre d'années:")
    annees = inputPositiveInt()
    print("Taux annuel:")
    taux = inputFloat()
    
    mensualite = calcul(montant, taux, annees)
    print(f'Mensualité : {mensualite}')

#Calcule de la mensualité du pret
#montant : montant total du pret
#taux : taux annuel du pret en %
#annees : nombre d'annees de l'emprunt
def calcul(montant : float, taux : float, annees : int):    
    T = ((taux)/100) / 12
    N = annees * 12
    result = pow((1+T), N)
    result = result / (pow((1+T), N) -1)
    result = result * montant * T
    return result
