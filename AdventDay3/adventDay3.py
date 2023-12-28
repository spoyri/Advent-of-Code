f = open("AdventDay3/input.txt", "r")
matrix = []
result = 0
for i in f:
    matrix.append([*i.strip('\n')])
y=0
while y < len(matrix):
    x=0
    while x < len(matrix[y]):
        num = ''
        delta = 0
        foundPart = False
        if (x+delta) < len(matrix[y]):
            if matrix[y][x+delta].isnumeric():
                while (x+delta) < len(matrix[y]) and matrix[y][x+delta].isnumeric():
                    num += matrix[y][x+delta]
                    for i in range(-1,2):
                        for j in range(-1,2):
                            deltay = y+j
                            deltax = x+delta+i
                            if deltay >= 0 and deltay < len(matrix) and deltax >= 0 and deltax < len(matrix[deltay]):
                                if not matrix[deltay][deltax].isalnum() and matrix[deltay][deltax] != '.':
                                    foundPart = True
                    delta += 1
                x += delta-1
                if foundPart:
                    result += int(num)
        x+=1
    y+=1
print(result)
