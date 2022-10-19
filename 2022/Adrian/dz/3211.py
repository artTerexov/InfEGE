
for i in range(1, 1000):
    n = i
    s = bin(i)[2:]
    if n % 2 == 0:
        s += '10'
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    if r > 516:
        print(i)
        break
