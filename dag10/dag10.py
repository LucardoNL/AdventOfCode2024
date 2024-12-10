with open('dag10input.txt') as f:
    input=f.read().splitlines()

matrix = [(int(v),(int(i),int(j))) for i,lst in enumerate(input) for j,v in enumerate(lst)]
startpunten = list(filter(lambda positie: positie[0] == 0, matrix ))

score = 0

def vindvalideburen(punt, eindpunt):
    global score
    x = punt[1][0]
    y = punt[1][1]
    stap = punt[0]
    potentieleburen = buren(punt)
    #print(stap, potentieleburen, eindpunt)
    for buur in potentieleburen:
        if buur[0] == 9 and stap == 8:
            if buur not in eindpunt:
                eindpunt.append(buur)
                score += 1
                #print('yes')
                
        elif buur[0] == stap+1:
            vindvalideburen(buur, eindpunt)
    return score
            
def buren(punt):
    max_rij = max([coord[1][0] for coord in matrix])
    max_kolom = max([coord[1][1] for coord in matrix])
    rij, kolom = punt[1][0], punt[1][1]
    mogelijke_bewegingen = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    buren = []
    for dr, dk in mogelijke_bewegingen:
        nieuwe_rij, nieuwe_kolom = rij + dr, kolom + dk
        if 0 <= nieuwe_rij <= max_rij and 0 <= nieuwe_kolom <= max_kolom:
            for waarde, (r, k) in matrix:
                if r == nieuwe_rij and k == nieuwe_kolom:
                    buren.append((waarde, (r, k)))
                    break
    return buren


for startpunt in startpunten:
    eindpunt = []
    #print(startpunt, eindpunt)
    vindvalideburen(startpunt, eindpunt)
# eindpunt = []
# vindvalideburen((0,(2,4)), eindpunt)

print(score)
