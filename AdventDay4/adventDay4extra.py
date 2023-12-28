f = open("AdventDay4/input.txt", "r")
result = 0
dic = {}
for a in range(219):
    dic[a+1]=1
for i in range(219):
    line = f.readline()
    score = 0
    cardnum = int(line.split(':')[0].split()[1])
    
    winnums = line.split(':')[1].split('|')[0].split()
    nums = line.split(':')[1].split('|')[1].split()
    for x in nums:
        if x in winnums:
            score += 1
    if score > 0:
        for s in range(cardnum + 1, cardnum + score + 1):
            dic[s] = dic[s] + dic[cardnum]
    result += dic[cardnum]
print(result) 
