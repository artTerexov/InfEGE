
for N in range(91, 1000):
    R = bin(N)[2:]
    for i in range(3):
        c = R.count('0')
        k = R.count('1')
        if c == k:
            R += R[-1]
        elif c > k:
            R += '1'
        else:
            R += '0'
    if int(R, 2) % 2 == 0 and int(R, 2) % 4 != 0:
        print(N)
        break





