from functools import cmp_to_key
f = open("AdventDay7\input.txt", "r")
result = 0
cardDict = {
    'A':14,
    'K':13,
    'Q':12,
    'J':11,
    'T':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2
}

def countcards(hand):
    dic = {}
    most = 0
    sec = 0
    for i in hand[0]:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic:
        if dic[i] > most:
            sec = most
            most = dic[i]
        elif dic[i] > sec:
            sec = dic[i]
    return (most, sec)

def handcomp(hand1, hand2):
    most1 = countcards(hand1)
    most2 = countcards(hand2)
    i = 0
    if most1[0] != most2[0]:
        return most1[0]-most2[0]
    elif most1[1] != most2[1]:
        return most1[1] - most2[1]
    else:
        while cardDict[hand1[0][i]] == cardDict[hand2[0][i]]:
            i+=1
    return cardDict[hand1[0][i]] - cardDict[hand2[0][i]]
hands = []
for i in f:
    hands.append((i.split()[0], i.split()[1]))
results = sorted(hands, key=cmp_to_key(handcomp))
for i in range(len(results)):
    result += int(results[i][1])*(i+1)
print(result)
