with open('files/demo') as f:
    s = [[int(j) for j in i.replace(';', ' ').split()] for i in f.readlines()]


buff = {0: 0}


for i in s:
    if all(sub in buff for sub in i[2:]):
        buff[i[0]] = i[1] + max(buff[sub] for sub in i[2:])

print(max(buff.values()))
