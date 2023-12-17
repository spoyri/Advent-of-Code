f=open("test.txt", "r")
textList = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    
}
result = 0
for i in range(0, 1000):
    string=f.readline()
    first = 1000
    firstValue = 0
    last = -1
    lastValue = 0
    for t in textList:
        index = string.find(t)
        rindex = string.find(t)
        if(index >= 0):
            if(index < first):
                first = index
                firstValue = textList[t]
            if(rindex > last):
                last = rindex
                lastValue = textList[t]
    add = int(str(firstValue) + str(lastValue))
    result += add
print(result)
