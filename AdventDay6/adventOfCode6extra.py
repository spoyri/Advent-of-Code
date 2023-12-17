f = open("AdventDay6\input.txt", "r")
line = f.readline()
time = int(''.join(line.split()[1:]))
line = f.readline()
record = int(''.join(line.split()[1:]))
wins = 0
for x in range(time+1):
    if x*(time-x) > record:
        wins += 1
print(wins)
    
