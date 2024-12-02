with open('dag1input.txt') as f:
    regels = f.read().splitlines() 

links = sorted([int(x) for y in regels for x in y.split()][::2])
rechts = sorted([int(x) for y in regels for x in y.split()][1::2])

deel1 = sum([abs(x-y) for x,y in zip(links,rechts)])
deel2 = sum([rechts.count(x)*x for x in links])

print(deel1)
print(deel2)