f = open("AdventDay6\input.txt", "r")
results = 1
line = f.readline()
times = [int(x) for x in line.split()[1:]]
line = f.readline()
records = [int(x) for x in line.split()[1:]]
for i in range(len(times)):
    wins = 0
    for x in range(times[i]+1):
        if x*(times[i]-x) > records[i]:
            wins += 1
    results *= wins
print(results)
    
