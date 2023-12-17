f=open("AdventDay2\input.txt", "r")
result = 0
for i in range(0, 100):
    string = f.readline()
    possible = True
    split = string.split(': ')
    gameNumber = int(split[0].split(' ')[-1])
    pulls = split[1].split('; ')
    for s in pulls:
        for v in s.split(', '):
            color = v.split(' ')[1][0]
            number = int(v.split(' ')[0])
            if color == 'r' and number > 12:
                possible = False
            if color == 'g' and number > 13:
                possible = False
            if color == 'b' and number > 14:
                possible = False
    if possible:
        result += gameNumber

print(result)
