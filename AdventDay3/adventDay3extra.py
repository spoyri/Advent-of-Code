f = open("AdventDay3/input.txt", "r")
matrix = []
result = 0
for i in f:
    matrix.append([*i.strip('\n')])
resultmatrix = []
for s in matrix:
    row = []
    for d in s:
        row.append([])
    resultmatrix.append(row)
y=0
while y < len(matrix):
    x=0
    while x < len(matrix[y]):
        num = ''
        delta = 0
        starx=-1
        stary=-1
        if (x+delta) < len(matrix[y]):
            if matrix[y][x+delta].isnumeric():
                while (x+delta) < len(matrix[y]) and matrix[y][x+delta].isnumeric():
                    num += matrix[y][x+delta]
                    for i in range(-1,2):
                        for j in range(-1,2):
                            deltay = y+j
                            deltax = x+delta+i
                            if deltay >= 0 and deltay < len(matrix) and deltax >= 0 and deltax < len(matrix[deltay]):
                                if matrix[deltay][deltax] == '*':
                                    starx=deltax
                                    stary=deltay
                    delta += 1
                if starx != -1:
                    resultmatrix[stary][starx].append(int(num))
                x += delta-1
        x+=1
    y+=1
for i in resultmatrix:
    for j in i:
        if len(j) == 2:
            result += j[0] * j[1]
print(result)
