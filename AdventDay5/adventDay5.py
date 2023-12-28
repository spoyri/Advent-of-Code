f = open("AdventDay5/input.txt", "r")
line = f.readline()
seeds = line.split()[1:]
seeds = [int(i) for i in seeds]
f.readline()
for i in range(7):
    f.readline()
    line = f.readline()
    ranges = []
    tempseeds = []
    while len(line) > 3:
        temp = line.split()
        temp = [int(s) for s in temp]
        ranges.append(temp)
        line = f.readline()
    for s in seeds:
        result = -1
        for rang in ranges:
            if s in range(rang[1], rang[1]+rang[2]):
                result = rang[0]+(s-rang[1])
        if result == -1:
            result = s
        tempseeds.append(result)
    seeds = tempseeds
print(min(seeds))
        
