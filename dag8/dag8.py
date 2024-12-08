import itertools as it

with open('dag8input.txt') as f:
    kaart = [list(rij) for rij in f.read().splitlines()]

def vindantennes(kaart):
    antennes = []
    for rij in kaart:
        for x,plek in enumerate(rij):
            if plek.isalnum():
                antennes.append([plek, (x, kaart.index(rij))])
    return antennes

def inLijn(antennes, deel):
    antennetypes = set([antenne[0] for antenne in antennes])
    paren=[]
    for type in antennetypes:
        print(type)
        specifiekeantennes = [antenne[1] for antenne in antennes if antenne[0] == type]
        if deel == 1:
            paren.append(vindparen(specifiekeantennes))
        else:
            paren.append(vindparen2(specifiekeantennes))
    print(len(paren[0]))

def vindparen(antennes):
    alleparen = list(it.combinations(antennes,2))
    antinodenopties = []
    for paar in alleparen:
        paar = list(paar)
        xafstand = paar[0][0] - paar[1][0]
        yafstand = paar[0][1] - paar[1][1]
        paar.append((xafstand, yafstand))
        antinodenopties.append((paar[0][0] + paar[2][0], paar[0][1] + paar[2][1]))
        antinodenopties.append((paar[1][0] - paar[2][0], paar[1][1] - paar[2][1]))
    return resonanties(antinodenopties)

def vindparen2(antennes):
    alleparen = list(it.combinations(antennes,2))
    antinodenopties = []
    for paar in alleparen:
        paar = list(paar)
        xafstand = paar[0][0] - paar[1][0]
        yafstand = paar[0][1] - paar[1][1]
        paar.append((xafstand, yafstand))
        for i in range(1,50):
            antinodenopties.append((paar[0][0] + paar[2][0]*i, paar[0][1] + paar[2][1]*i))
            antinodenopties.append((paar[1][0] - paar[2][0]*i, paar[1][1] - paar[2][1]*i))
        antinodenopties.append((paar[0][0],paar[0][1]))
        antinodenopties.append((paar[1][0],paar[1][1]))
    return resonanties(antinodenopties)
            
antinoden = set()

def resonanties(antinodenopties):
    maxX, maxY = len(kaart[0]), len(kaart)
    filterparen = [paar for paar in antinodenopties if paar[0] < maxX and paar[0] >= 0]
    filterparen = [paar for paar in filterparen if paar[1] < maxY and paar[1] >= 0]
    antinoden.update([paar for paar in filterparen])
    return antinoden

def deel1(kaart):
    antennes = vindantennes(kaart)
    inLijn(antennes, 1)

def deel2(kaart):
    antennes = vindantennes(kaart)
    inLijn(antennes, 2)

deel2(kaart)