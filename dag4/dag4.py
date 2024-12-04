import re
from collections import defaultdict

with open('dag4input.txt') as f:
    input = f.read()
    regels = input.splitlines()
    kolommen = ["".join(kol) for kol in zip(*regels)]
    diagonaal1 = defaultdict(list)
    diagonaal2 = defaultdict(list)
    for x in range(len(regels)):
        for y in range(len(kolommen)):
            diagonaal1[x-y].append(list(regels)[x][y])
            diagonaal2[x+y].append(list(regels)[x][y])
    diagonalen1 = diagonaal1.values()
    diagonalenVanLengte1 = [diagonaal for diagonaal in diagonalen1 if len(diagonaal) >= 4]
    diagonalenstring1 = ' '.join(''.join(diag) for diag in diagonalenVanLengte1)
    diagonalen2 = diagonaal2.values()
    diagonalenVanLengte2 = [diagonaal for diagonaal in diagonalen2 if len(diagonaal) >= 4]
    diagonalenstring2 = ' '.join(''.join(diag) for diag in diagonalenVanLengte2)

regelxmassen = len(re.findall(r'(?=(XMAS|SAMX))',' '. join(regels)))
kolomxmassen = len(re.findall(r'(?=(XMAS|SAMX))',' '.join(kolommen)))
diag1xmassen = len(re.findall(r'(?=(XMAS|SAMX))',diagonalenstring1))
diag2xmassen = len(re.findall(r'(?=(XMAS|SAMX))',diagonalenstring2))

print(regelxmassen+  kolomxmassen+ diag1xmassen+ diag2xmassen)

#deel 2
with open('dag4input.txt') as f:
    input = f.read()
    regels = input.splitlines()

regellengte = len(regels[0]) 
kolomlengte = len(regels)

xmassengevonden = 0

for i in range(1, kolomlengte-1):
    for j in range(1, regellengte-1):
        if regels[i][j] == 'A':
            d1 = regels[i-1][j-1] + regels[i][j] + regels[i+1][j+1]
            d2 = regels[i-1][j+1] + regels[i][j] + regels[i+1][j-1]
            if (d1 == 'MAS' or d1 == 'SAM') and (d2 == 'MAS' or d2 == 'SAM'):
                xmassengevonden += 1 

print(xmassengevonden)
