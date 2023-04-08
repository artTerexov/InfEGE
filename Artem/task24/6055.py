with open('files/6055.txt') as f:
    a = f.read()
m = 0
c = 0
for i in range(len(a)):
    if a[i] == 'F':
        k = i + 1
        s = 'F'
        kk = 0
        while True:
            s += a[k]
            if a[k] == 'E':
                kk += 1
            if a[k] == 'F' and kk >= 5:
                flag = True
                for z in range(1, len(s.split('E')) - 1):
                    b = s.split('E')
                    if b[z].count('A') != 1:
                        flag = False
                        break
                if flag:
                    m = max(len(s), m)
            k += 1
            if k == (len(a) + 1):
                break
print(m)
