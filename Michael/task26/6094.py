
def func(file, k, m):
    file = sorted(file, reverse=True)
    buff = []
    i = 0
    block = []
    while i < len(file):
        if len(block) == 0:
            block = [file.pop(0)]
        elif block[-1][0] - file[i][0] >= k and block[-1][1] != file[i][1] and len(block) != m:
            block.append(file.pop(i))
            i = 0
        elif len(block) == m:
            buff.append(len(block))
            block.clear()
            i = 0
        else:
            i += 1
            if i == len(file) and len(file) != 0:
                buff.append(len(block))
                block.clear()
                i = 0

    buff.append(len(block))
    return buff


with open("files/6094.txt") as f:
    a = [[int(i.split()[0]), i. split()[1]] for i in f.readlines()]

result = func(a, 20, 15)
print("Ответа на основной файл:", len(result), result.count(max(result)))


with open("files/6094_test") as f:
    a = [[int(i.split()[0]), i. split()[1]] for i in f.readlines()]

result = func(a, 5, 3)
print("Ответа на тестовый файл:", len(result), result.count(max(result)))