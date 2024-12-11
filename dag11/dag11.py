with open('dag11input.txt') as f:
    input = f.read().split(' ')

print(input)

def deel1(blinks):
    stenen = input[:]
    for _ in range(0,blinks):
        stenenkopie = []
        for steen in stenen:
            if steen == '0':
                stenenkopie.append('1')
            elif len(steen) % 2 == 0:
                steenlen = int(len(steen)/2)
                #print(steen, len(steen), steenlen, steen[-steenlen:])
                nieuwesteen = steen[-steenlen:]
                stenenkopie.append(steen[:steenlen])
                stenenkopie.append(str(int(nieuwesteen)))
            else:
                stenenkopie.append(str(int(steen)*2024))
        stenen = stenenkopie[:]
        #print(stenen, len(stenen))
    return stenen

print(len(deel1(25)))