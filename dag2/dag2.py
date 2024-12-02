with open('dag2input.txt') as f:
    rapporten = f.read().splitlines() 

veilig1 = 0
veilig2 = 0

for rapport in rapporten:
    rapport = [int(x) for x in rapport.split()]
    if sorted(rapport) == rapport or sorted(rapport, reverse = True) == rapport:
        verschillen = [sorted(rapport)[i+1]-sorted(rapport)[i] for i in range(len(sorted(rapport))-1)]
        if (max(verschillen) < 4) and (min(verschillen) > 0):
            veilig1 += 1

print('Veilig 1: ', veilig1)

for rapport in rapporten:
    rapport = [int(x) for x in rapport.split()]
    for level in range(len(rapport)):
        rapportKopie = rapport[:]
        #print (rapport, rapportKopie, level, range(len(rapport)))
        rapportKopie.pop(level)
        if sorted(rapportKopie) == rapportKopie or sorted(rapportKopie, reverse = True) == rapportKopie:
            verschillen = [sorted(rapportKopie)[i+1]-sorted(rapportKopie)[i] for i in range(len(sorted(rapportKopie))-1)]
            if (max(verschillen) < 4) and (min(verschillen) > 0):
                veilig2 += 1
                break
                
print('Veilig 2: ', veilig2)
