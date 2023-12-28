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
expanded = []
for i in range(len(matrix)):
  row = []
  for j in range(len(matrix[0])):
    if j in columns:
      row.append(matrix[i][j])
    row.append(matrix[i][j])
  if i in rows:
    expanded.append(row)
  expanded.append(row)
index=0
dic = {}
sum = 0
for i in range(len(expanded)):
  row = []
  for j in range(len(expanded[0])):
    if expanded[i][j] == '#':
      dic[index]=(i,j)
      index += 1
for i in range(len(dic)):
  for j in range(i+1, len(dic)):
    first = dic[i]
    second = dic[j]
    sum += abs(first[0] - second[0]) + abs(first[1] - second[1])
print(sum)