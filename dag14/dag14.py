from operator import countOf
from time import sleep
import copy

with open('dag14input.txt') as f:
    robots = f.read().splitlines()

tijd = 100
bordbreedte = 101
halfbreed = 50
bordlengte = 103
halflang = 51
eindposities = []

q1,q2,q3,q4 = 0,0,0,0

def moverobot(robot):
    pos = robot[0].split(',')
    xpos = int(pos[0])
    ypos = int(pos[1])
    speed = robot[1].split(',')
    xspeed = int(speed[0])
    yspeed = int(speed[1])
 
    xeindloc = (xpos + xspeed * tijd) % bordbreedte
    yeindloc = (ypos + yspeed * tijd) % bordlengte
    eindposities.append((xeindloc, yeindloc))
    #print(robot, (xeindloc, yeindloc))

def inkwadrant(positie):
    global q1,q2,q3,q4

    rij, kolom = positie
    if rij == halfbreed or kolom == halflang:
        pass
    if rij < halfbreed and kolom < halflang:
        q1 +=1
        #print(positie, 'q1')
    elif rij < halfbreed and kolom > halflang:
        q2 +=1
        #print(positie, 'q2')
    elif rij > halfbreed and kolom < halflang:
        q3 +=1
        #print(positie, 'q3')
    elif rij > halfbreed and kolom > halflang:
        q4 +=1
        #print(positie, 'q4')
    
for i,robot in enumerate(robots):
    robot = robot.split(' ')
    robot[0] = robot[0][2:]
    robot[1] = robot[1][2:]
    moverobot(robot)
    robots[i] = robot

for positie in eindposities:
    inkwadrant(positie)

print(q1*q2*q3*q4)

def moverobotstaps(robot, stap):
    pos = robot[0].split(',')
    xpos = int(pos[0])
    ypos = int(pos[1])
    speed = robot[1].split(',')
    xspeed = int(speed[0])
    yspeed = int(speed[1])
 
    nieuwxpos = (xpos + xspeed * stap) % bordbreedte
    nieuwypos = (ypos + yspeed * stap) % bordlengte
    return (nieuwxpos, nieuwypos)

startbeeld = [['_' for _ in range(101)] for _ in range(103)]

for j in range(10000):
    robotlijst = []
    robotset = set()
    for i, robot in enumerate(robots):
        (x,y) = moverobotstaps(robot, j)
        robotlijst.append((x,y))
        robotset.add((x,y))
    if len(robotlijst) == len(robotset):
        print(j)
        break
    print(j, len(robotlijst) , len(robotset))