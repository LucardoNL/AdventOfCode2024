import copy

with open('dag6input.txt') as f:
    kaartregels = [list(regels.strip()) for regels in f]
    
with open('dag6input.txt') as f:
    kaartregels2 = [list(regels.strip()) for regels in f]

def beweging(kaartregels):
    pos = [0,0]
    doelStap = [0,0]
    pos = haalPositie(pos, kaartregels)
    kaartregels[pos[1]][pos[0]] = 'X'
    richtingen = ['omhoog', 'rechts', 'omlaag', 'links']
    richting = richtingen[0]
    opBord = True
    looplijst = set()
    while opBord == True:
        opBord = loopCheck(richting, pos, looplijst)
        if richting == 'omhoog' and pos[1]-1 >= 0:
                doelStap = [pos[0],pos[1]-1]
        elif richting == 'rechts' and pos[0]+1 < len(kaartregels[0]):
                doelStap = [pos[0]+1,pos[1]]
        elif richting == 'omlaag' and pos[1]+1 < len(kaartregels):
                doelStap = [pos[0],pos[1]+1]
        elif richting == 'links' and pos[0]-1 >= 0:
                doelStap = [pos[0]-1,pos[1]]
        else:
            opBord = False
        try:
             bordPlek = kaartregels[doelStap[1]][doelStap[0]]
        except:
             pass
        if bordPlek == '#':
             richtingen.pop(0)
             richtingen.append(richting)
             richting = richtingen[0]
        else:
            pos = doelStap
        #print(bordPlek, doelStap, richting, richtingen)
        kaartregels[pos[1]][pos[0]] = 'X'
    return kaartregels



def haalPositie(pos, kaartregels):
    for regel in kaartregels:
        if '^' in regel:
            #print(regel.index('^'), kaartregels.index(regel))
            pos[0],pos[1] = regel.index('^'), kaartregels.index(regel)
        else:
             pass
    return pos

def deel1(kaartregels):
    kaartregels = beweging(kaartregels)
    Xen = 0
    for regel in kaartregels:
        for teken in regel:
            if teken ==  'X':
                Xen += 1
    print(Xen)

def loopCheck(richting, pos, looplijst):
     stap = (richting, tuple(pos))
     if stap in looplijst:
          loopstappen.append(stap)
          return False
     else:
          looplijst.add(stap)
          return True

loopstappen = []

deel1(kaartregels)

def deel2():
    for regel in kaartregels:
        kolindex = 0
        for teken in regel:
            if teken == 'X':
                nieuwKaartregels = copy.deepcopy(kaartregels2)
                if nieuwKaartregels[kaartregels.index(regel)][kolindex] == '^':
                    pass
                nieuwKaartregels[kaartregels.index(regel)][kolindex] = '#'
                #print(regel, teken, kaartregels2.index(regel),kolindex)
                #print(nieuwKaartregels)
                beweging(nieuwKaartregels)
                del nieuwKaartregels
                print(kaartregels.index(regel),kolindex)
            else:
                 print('Geen X')
                 pass
            kolindex +=1
    print(loopstappen, len(loopstappen))

deel2()
#print(kaartregels)


