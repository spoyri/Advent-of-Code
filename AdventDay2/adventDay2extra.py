f=open("AdventDay2/input.txt", "r")
result = 0
for i in range(0, 100):
    string = f.readline()
    reds = 0
    greens = 0
    blues = 0
    split = string.split(': ')
    gameNumber = int(split[0].split(' ')[-1])
    pulls = split[1].split('; ')
    for s in pulls:
        for v in s.split(', '):
            color = v.split(' ')[1][0]
            number = int(v.split(' ')[0])
            if color == 'r' and number > reds:
                reds = number
            if color == 'g' and number > greens:
                greens = number
            if color == 'b' and number > blues:
                blues = number
    result += reds * greens * blues

print(result)
