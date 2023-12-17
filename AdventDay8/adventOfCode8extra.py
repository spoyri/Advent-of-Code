f = open("AdventDay8\input.txt", "r")
dirs = list(f.readline())[:-1]
f.readline()
dic = {}

def allInZ(zone):
    result = 0
    for i in zone:
        if i[2] == 'Z':
            result += 1
    if result >= 4:
        print(zone, result)
    return result
zones = []
for i in f:
    name = i.split('=')[0][:3]
    moves = i.split('=')[1][2:10]
    moves = (moves.split(',')[0], moves.split(',')[1].strip())
    dic[name] = moves
    if name[2] == 'A':
        zones.append(name)
print(zones)
i = 0
steps = 0
while allInZ(zones) != len(zones):
    templist = []
    for s in zones:
        if dirs[i] == 'L':
            templist.append(dic[s][0])
        else:
            templist.append(dic[s][1])
    zones = templist
    if steps < 2:
        print(zones)
    i+=1
    if i == len(dirs):
        i=0
    steps += 1
print(steps)

