f=open("AdventDay11/input.txt", "r")
matrix = [[y for y in x if '\n' not in y] for x in f.readlines()]
rows=[]
columns=[]
for i in range(len(matrix)):
  double = True
  for j in range(len(matrix[0])):
    if matrix[i][j] == '#':
      double=False
  if double:
    rows.append(i)
for j in range(len(matrix[0])):
  double = True
  for i in range(len(matrix)):
    if matrix[i][j] == '#':
      double=False
  if double:
    columns.append(j)
index=0
dic = {}
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == '#':
      rowsbefore = [x for x in rows if x < i]
      newi=i+len(rowsbefore)*999999
      colsbefore = [x for x in columns if x < j]
      newj=j+len(colsbefore)*999999
      dic[index]=(newi,newj)
      index += 1
sum = 0
print(dic)
for i in range(len(dic)):
  for j in range(i+1, len(dic)):
    first = dic[i]
    second = dic[j]
    sum += abs(first[0] - second[0]) + abs(first[1] - second[1])
print(sum)