import re

with open('dag9input.txt') as f:
    input = f.read()

def deel1():
    blocks = []
    id = 0
    for index, diskmap in enumerate(input):
        if index % 2 == 0:
            for x in range(int(diskmap)):
                blocks.append(id)
            id += 1
        else:
            for x in range(int(diskmap)):
                blocks.append(" ")
    positie = 0
    while " " in blocks:
        laatstewaarde = blocks.pop()
        try:
            positie = blocks.index(" ")
        except:
            break
        blocks[positie] = laatstewaarde
    checksum = sum([int(waarde)*plek for plek, waarde in enumerate(blocks)])
    return checksum

def deel2():
    #mislukte poging
    blocks = []
    id = 0
    for index, diskmap in enumerate(input):
        if index % 2 == 0:
            for x in range(int(diskmap)):
                blocks.append(id)
            id += 1
        else:
            for x in range(int(diskmap)):
                blocks.append(" ")
    print(blocks)
    metablokken = samenvoegenblokken(blocks)
    nieuweblokken = metablokken[:]
    for block in reversed(metablokken):
        bloklengte = len(block) / len(str((metablokken.index(block))))
        if bloklengte > 0 and block[0] != " ":
            try:
                print(nieuweblokken)
                leegblok = next(leegblok for leegblok in nieuweblokken if len(leegblok) >= bloklengte and leegblok[0] == ' ' and nieuweblokken.index(leegblok) < nieuweblokken.index(block) )
                leegblokpos = nieuweblokken.index(leegblok)
                blockpos = nieuweblokken.index(block)
                nieuweblokken[blockpos] = ' '*bloklengte
                nieuweblokken[leegblokpos] = leegblok[bloklengte:]
                nieuweblokken.insert(leegblokpos, block)
            except:
                pass
        else:
            pass
    nieuweblokken = filter(None, nieuweblokken)
    checksum = 0 
    for plek, waarde in enumerate(nieuweblokken):
        try:
            checksum += plek*int(waarde)
        except:
            pass
    print(checksum)

def samenvoegenblokken(blocks):
    resultaat = []
    tijdelijke_string = str(blocks[0])
    for i in range(1, len(blocks)):
        if blocks[i] == blocks[i - 1]:
            tijdelijke_string += str(blocks[i])
        else:
            resultaat.append(tijdelijke_string)
            tijdelijke_string = str(blocks[i])
    resultaat.append(tijdelijke_string)
    return resultaat

def deel2b():
    blocks = []
    id = 0
    for index, diskmap in enumerate(input):
        if index % 2 == 0:
            blocks.append((id, int(diskmap)))
            id += 1
        else:
            blocks.append((" ", int(diskmap)))
    nieuweblokken = blocks[:]
    print('blocks klaar')
    
    for blok in reversed(blocks):
        if blok[0] != ' ':
            try:
                leegblok = next(leegblok for leegblok in nieuweblokken if leegblok[1] >= blok[1] and leegblok[0] == ' 'and nieuweblokken.index(leegblok) < nieuweblokken.index(blok))
                leegblokpos = nieuweblokken.index(leegblok)
                blokpos = nieuweblokken.index(blok)
                nieuweblokken[blokpos] = ((' ', blok[1]))
                nieuweblokken[leegblokpos] = (' ', leegblok[1]-blok[1])
                nieuweblokken.insert(leegblokpos, blok)
            except:
                pass
        else:
            pass

    print('nieuwe blokken klaar')
    finaleblokken = []
    for blok in nieuweblokken:
         for _ in range(blok[1]):
            if blok[0] == ' ':
                finaleblokken.append(0)
            else:
                finaleblokken.append(blok[0])
    checksum = sum([int(waarde)*plek for plek, waarde in enumerate(finaleblokken)])
    return  checksum



print(deel2b())


