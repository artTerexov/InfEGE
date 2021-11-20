y = bin(204)[2:]
for N in range(1, 257):
    x = bin(N-1)[2:]
    x = '0' * (8 - len(x)) + x
    buff = ''
    for i in range(len(x)):
        if x[i] == '1':
            buff += '0'
        else:
            buff += '1'
    if buff == y:
        print(N)
        break