with open("files/5387") as f:
    a = f.readline()

i = 0
buff = []
maxx = 0
while i < len(a) - 1:
    if a[i] in "ABC" and a[i + 1] in "123":
        buff.append(a[i])
        buff.append(a[i + 1])
        i += 2
    elif a[i] in "ABC" and a[i + 1] in "ABC":
        i += 1
        maxx = max(maxx, len(buff) // 2)
        buff.clear()
    else:
        i += 2
        maxx = max(maxx, len(buff) // 2)
        buff.clear()


print(maxx)