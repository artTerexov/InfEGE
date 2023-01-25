from itertools import product


def decreasing(x) -> bool:
    flag = True
    for j in range(len(x) - 1):
        if x[j] <= x[j + 1] or int(x[j]) % 2 == int(x[j + 1]) % 2:
            flag = False

    return flag


a = product("0123456789", repeat=6)
c = 0

for i in a:
    el = ''.join(i)
    if el[0] != 0 and decreasing(el):
        c += 1
        # print(c, el)


print(c)