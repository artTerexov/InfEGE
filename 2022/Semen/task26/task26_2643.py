with open('files/2643.txt') as f:
    s = f.read().strip().split()

coins = [int(s[i]) for i in range(1, len(s))]
numOfPairs = 0
for i in coins:
    diff = 100 - i
    if diff in coins:
        numOfPairs += 1
        coins.remove(i)
        coins.remove(diff)
print(numOfPairs)