star = [''] + [str(i) for i in range(100)]

for i in star:
    s = int('12' + i + '6789')
    if s % 39 == 0:
        print(s, s // 39)
