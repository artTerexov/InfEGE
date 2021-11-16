for n in range(1, 257):
    b = bin(n-1)[2:]
    b = "0" * (8 - len(b)) + b
    reverse = ''
    for c in b:
        if c == '1':
            reverse += '0'
        elif c == '0':
            reverse += '1'
    r = int(reverse, 2)
    if r == 204:
        print(n)