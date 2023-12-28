f = open("AdventDay8/input.txt", "r")
dirs = list(f.readline())[:-1]
f.readline()
dic = {}
for i in f:
    name = i.split('=')[0][:3]
    moves = i.split('=')[1][2:10]
    moves = (moves.split(',')[0], moves.split(',')[1].strip())
    dic[name] = moves
zone = 'AAA'
i = 0
steps = 0
while zone != 'ZZZ':
    if dirs[i] == 'L':
        zone = dic[zone][0]
    else:
        zone = dic[zone][1]
    if i < len(dirs)-1:
        i+=1
    else:
        i=0
    steps += 1
print(steps)

