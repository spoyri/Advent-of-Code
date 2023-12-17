f = open("AdventDay4\input.txt", "r")
result = 0
for i in range(219):
    line = f.readline()
    score = 0
    winnums = line.split(':')[1].split('|')[0].split()
    nums = line.split(':')[1].split('|')[1].split()
    for x in nums:
        if x in winnums:
            if score > 0:
                score = score * 2
            else:
                score = 1
    result += score
print(result) 
