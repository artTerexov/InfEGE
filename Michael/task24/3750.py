
# Решение через словарь
# def oftenWord(x):
#     result = dict()
#     # result = ['', 0]
#     for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         result[j] = 0
#         for i in range(len(x) - 2):
#             if (x[i] == x[i + 2]) and x[i + 1] == j:
#                 result[j] += 1
#     return result


# 'A': 43


def oftenWord(x):
    result = ['', 0]
    for j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        c = 0
        for i in range(len(x) - 2):
            if (x[i] == x[i + 2]) and x[i + 1] == j:
                c += 1
        if c > result[1]:
            result[0] = j
            result[1] = c
    return result



with open("files/3750") as a:
    s = a.readline()

print(max(oftenWord(s)))

# B 1461
