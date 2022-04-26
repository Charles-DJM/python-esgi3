#Autheur: Charles de JAHAM
#Date: 24/04/2022

from inputFunc import inputPositiveInt

def ex8():
    print("---Le plus grand---")
    
    tab = []
    for i in range(0, 10):
        print(f'Entrez le nombre numero {i}: ')
        tab.append(inputPositiveInt())
    
    result = max(tab)
    print(f'Le plus grand de ces nombres est : {result}')
    print(f'C\'etait le nombre numéro {tab.index(result)}')