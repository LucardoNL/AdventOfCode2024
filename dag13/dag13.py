import re

with open('dag13input.txt') as f:
    input = f.read().splitlines()

def runmachine(deel):
    for line in input:
        if 'A:' in line:
            a = re.findall(r'(\d+)', line)
        elif 'B:' in line:
            b = re.findall(r'(\d+)', line)
        elif 'Prize' in line:
            doel = re.findall(r'(\d+)', line)
            if deel == 1:
                solve(a,b,doel)
            elif deel == 2:
                doel[0] = int(doel[0]) + 10000000000000
                doel[1] = int(doel[1]) + 10000000000000
                solve(a,b,doel)

    return kosten

def solve(a,b,doel):
    global kosten
    Ax,Ay = int(a[0]),int(a[1])
    Bx,By = int(b[0]),int(b[1])
    Px,Py = int(doel[0]),int(doel[1])
    print(Px,Py)
    y,r = divmod((Ay * Px - Ax * Py), (Ay * Bx - Ax * By))
    
    if r == 0:
        x = (Px - Bx * y) // Ax
        kosten += 3*x + y

kosten = 0

print(runmachine(1))
kosten = 0
print(runmachine(2))
        

