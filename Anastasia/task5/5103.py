count = set()
for i in range(1, 1000):
    N = bin(i)[2:]
    if i % 2 == 0:
        N = '1' + N + '10'
    else:
        N = '11' + N + '0'
    R = int(N, 2)
    if 800 <= R <= 1500:
        count.add(R)

print(len(count))