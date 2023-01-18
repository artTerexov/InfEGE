x = [i for i in range(44)]


for i in x:
    num_1 = 1 * 44 ** 3 + i * 44 ** 2 + 2 * 44 + 3
    num_2 = 3 * 44 ** 3 + 2 * 44 ** 2 + i * 44 + 1
    if (num_1 + num_2) % 42 == 0:
        print(i, (num_1 + num_2) / 42)

