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
    for s in range(len(seeds))[::2]:
        added = 0
        seedstart = seeds[s]
        seedend = seeds[s] + seeds[s+1]
        for rang in ranges:
            sourceend = rang[1]+rang[2]
            if seedend > rang[1] and (seeds[s] < sourceend):
                start = max(seeds[s], rang[1])
                end = min(seedend, sourceend)
                dist = end - start
                tempseeds.append(start + (rang[0]-rang[1]))
                tempseeds.append(dist)
                added += 1
        if added == 0:
            tempseeds.append(seedstart)
            tempseeds.append(seeds[s+1])
    seeds = tempseeds
print(min(seeds[::2]))
        
