with open('files/27_A (1).txt') as f:
    s = [int(i) for i in f.read().strip().split('\n')]

s.pop(0)


