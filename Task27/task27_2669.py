import time

startTime = time.time()
with open('Files/27_2669_a.txt') as f:
    s = f.read().strip().split('\n')

s.pop(0)
g = [int(i) for i in s]
gSet = set()

for i in g:
    if i % 2 != 0:
        gSet.add(i)

sorted(gSet)
result = -1

for i in range(0, len(g) - 6):
    for j in gSet:
        if j in g[i+6:len(g)]:
            number = g[i] * j
            if number % 2 != 0:
                if result == -1:
                    result = number
                else:
                    result = min(result, number)
                break
        else:
            continue

print(result)

print("--- %s seconds ---" % (time.time() - startTime))
