buff = set()
for i in range(1, 100000):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '1' + n + '10'
    else:
        n = '11' + n + '0'
    R = int(n, 2)
    if 800 <= R <= 1500:
        buff.add(R)
print(len(buff))