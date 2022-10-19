d = [int(x) for x in open('files/3775_A.txt')]
c = 0
d.pop(0)
d.sort(reverse=True)
for i in range(len(d)):
    for j in range(i + 1, len(d)):
        for q in range(j + 1, len(d)):
            for w in range(q + 1, len(d)):
                if (d[i] + d[j] + d[q] + d[w]) % 6 == 0:
                    c = max((d[i] + d[j] + d[q] + d[w]), c)
                    print(d[i] + d[j] + d[q] + d[w], d[i], d[j], d[q], d[w])
print(c)