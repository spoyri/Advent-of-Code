f = open("AdventDay8\input.txt", "r")
import math
dirs = list(f.readline())[:-1]
f.readline()
dic = {}

def allInZ(zone):
    result = 0
    for i in zone:
        if i[2] == 'Z':
            result += 1
    return result
zones = []
for i in f:
    name = i.split('=')[0][:3]
    moves = i.split('=')[1][2:10]
    moves = (moves.split(',')[0], moves.split(',')[1].strip())
    dic[name] = moves
    if name[2] == 'A':
        zones.append(name)
roads = len(zones)
loopstart = {}
loopend = {}
i = 0
steps = 0
while len(loopend) != roads:
    templist = []
    for s in range(len(zones)):
        zone = zones[s]
        if not zone == 's':
            if zone[2] == 'Z' and s in loopstart:
                loopend[s] = steps
                templist.append('s')
            else:
                if zone[2] == 'Z':
                    loopstart[s] = steps
                if dirs[i] == 'L':
                    templist.append(dic[zone][0])
                else:
                    templist.append(dic[zone][1])
        else:
            templist.append('s')
    zones = templist
    i+=1
    if i == len(dirs):
        i=0
    steps += 1
result = 1
print(loopstart)
for i in loopstart:
    gcd = math.gcd(int(result), int(loopstart[i]))
    result *= loopstart[i]/gcd
print(result)
found = False
result = loopend[roads-1]
while not found:
    found = True
    result += loopend[roads-1]-loopstart[roads-1]
    lista = [result]
    for i in range(len(loopstart)-1):
        loop = loopend[i]-loopstart[i]
        lista.append((result-loopstart[i]) % loop)
        if (result-loopstart[i]) % loop != 0:
            found = False
    
print(result)

