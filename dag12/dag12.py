from operator import countOf

with open('dag12input.txt') as f:
    input = f.read().splitlines()

vakken={}
groepsteller = 0

for kolomindex, regel in enumerate(input):
    for rijindex, teken in enumerate(regel):
        vakken[(rijindex,kolomindex)] = {'teken': teken, 'groep': '', 'hekken':0 }

def bepaal_buren(vak):
    buren = {}
    richtingen = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dk in richtingen:
        buur_rij = vak[0] + dr
        buur_kolom = vak[1] + dk
        if (buur_rij, buur_kolom) in vakken:
            buren[(buur_rij, buur_kolom)] = vakken[(buur_rij, buur_kolom)]
    ##print('vak:', vak, 'buren: ', [v['teken'] for k,v in buren.items()])
    return buren

#floodfill algoritme vanuit reddit
def flood_fill(grid, start):
    region = set([start])
    symbol = grid[start]['teken']
    queue = [start]
    while queue:
        pos = queue.pop()
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = tuple((pos[0] + d[0], pos[1] + d[1]))
            ##print(pos, new_pos, d)
            if new_pos in grid and new_pos not in region and grid[new_pos]['teken'] == symbol:
                region.add(new_pos)
                queue.append(new_pos)
    return region

#bepaal hekken
for vak, inhoud in vakken.items():
    buren = bepaal_buren(vak)
    aantalgelijkeburen = countOf([v['teken'] for k,v in buren.items()], inhoud['teken'])
    vakken[vak]['hekken'] = 4 - aantalgelijkeburen

regios = []
ontoegewezen_vakken = set(vakken)
while len(ontoegewezen_vakken) > 0:
    start = ontoegewezen_vakken.pop()
    regio = flood_fill(vakken, start)
    ontoegewezen_vakken -= regio
    regios.append(regio)

prijs = 0

for regio in regios:
    ##print(regio)
    hekken = 0
    for veld in regio:
        ##print(veld)
        hekken += vakken[veld]['hekken']
    prijs += hekken*len(regio)

#print(prijs)

def get_teken(xy):
    return vakken.get(xy, {}).get('teken', ' ')

def hoekenzoeken(regio):
    hoeken = 0
    for veld in regio:
        veldteken = vakken[veld]['teken']
        ##print(veldteken)
        x,y = veld[0],veld[1]

        # Set 1 (rechts en onder)
        set1 = [get_teken((x + 1, y)), get_teken((x, y + 1))]
        set1hoek = get_teken((x + 1, y + 1))

        # Set 2 (links en boven)
        set2 = [get_teken((x - 1, y)), get_teken((x, y - 1))]
        set2hoek = get_teken((x - 1, y - 1))

        # Set 3 (rechts en boven)
        set3 = [get_teken((x + 1, y)), get_teken((x, y - 1))]
        set3hoek = get_teken((x + 1, y - 1))

        # Set 4 (links en onder)
        set4 = [get_teken((x - 1, y)), get_teken((x, y + 1))]
        set4hoek = get_teken((x - 1, y + 1))

        #print(veld, veldteken, set1, set1hoek, set2, set2hoek, set3, set3hoek, set4, set4hoek)
        if veldteken not in set1:
            hoeken += 1
            #print('buitenhoek 1')
        if veldteken not in set2:
            hoeken += 1
            #print('buitenhoek 2')
        if veldteken not in set3:
            hoeken += 1
            #print('buitenhoek 3')
        if veldteken not in set4:
            hoeken += 1 
            #print('buitenhoek 4')  
        if veldteken == set1[0] and veldteken == set1[1] and veldteken != set1hoek:
            hoeken += 1
            #print('binnenhoek 1')
        if veldteken == set2[0] and veldteken == set2[1] and veldteken != set2hoek:
            hoeken += 1
            #print('binnenhoek 2')
        if veldteken == set3[0] and veldteken == set3[1] and veldteken != set3hoek:
            hoeken += 1
            #print('binnenhoek 3')
        if veldteken == set4[0] and veldteken == set4[1] and veldteken != set4hoek:
            hoeken += 1
            #print('binnenhoek 4')
    
    return hoeken

prijs2 = 0
for regio in regios:
    #if (7, 3) in regio:
    hoeken = hoekenzoeken(regio)
    #print(regio, len(regio), hoeken)
    prijs2 += len(regio) * hoeken
    

print(prijs2)


