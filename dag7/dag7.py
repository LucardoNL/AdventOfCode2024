from operator import add, mul, concat
from functools import reduce

with open('dag7input.txt') as f:
    rekenregels = f.read().splitlines()
    rekenregels = [tuple(regel.split(':')) for regel in rekenregels]

def rekenmachine(rekenregel, deel):
    doelwaarde = int(rekenregel[0])
    rekenwaarden = list(map(int, rekenregel[1].lstrip().split(' ')))
    if deel == 1:  
        permutaties = reduce(permutator, [[rekenwaarden[0]]]+rekenwaarden[1:])
    elif deel == 2:
        permutaties = reduce(permutator2, [[rekenwaarden[0]]]+rekenwaarden[1:])
    if doelwaarde in permutaties:
        return doelwaarde
    else:
        return 0
        
def permutator(getallen, rekenwaarden):
    return [operatie(getal, rekenwaarden) for getal in getallen for operatie in [add, mul]]

def permutator2(getallen, rekenwaarden):
    return [operatie(getal, rekenwaarden) for getal in getallen for operatie in (add, mul, lambda a,b:  int(str(a)+str(b)))]

uitkomst = 0
for regel in rekenregels:
    uitkomst += rekenmachine(regel, 1)

print('Deel1 ', uitkomst)

uitkomst2 = 0
for regel in rekenregels:
    uitkomst2 += rekenmachine(regel, 2)

print('Deel 2: ', uitkomst2) 

