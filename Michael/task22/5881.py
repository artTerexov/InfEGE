with open('files/5881') as f:
    s = [[int(j) for j in i.replace(';', ' ').split()] for i in f.readlines()]

buff = {0: 0}

while len(buff) - 1 != len(s):
    for i in s:
        if all(sub in buff for sub in i[2:]):
            buff[i[0]] = i[1] + max(buff[sub] for sub in i[2:])

c = 0
for key, value in buff.items():
    if buff.get(1) - 26 <= value <= buff.get(1) - 26 + 40:
        print(key)
        c += 1
