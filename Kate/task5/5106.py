buff = set()
for N in range(1, 100000):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = '1' + n + '10'
    else:
        n = '11' + n + '0'
    R = int(n, 2)
    if 800 <= R <= 1500:
        buff.add(R)

print(len(buff))
