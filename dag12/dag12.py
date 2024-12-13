from operator import countOf

with open('dag12test.txt') as f:
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
    #print('vak:', vak, 'buren: ', [v['teken'] for k,v in buren.items()])
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
            #print(pos, new_pos, d)
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
    #print(regio)
    hekken = 0
    for veld in regio:
        #print(veld)
        hekken += vakken[veld]['hekken']
    prijs += hekken*len(regio)

print(prijs)
