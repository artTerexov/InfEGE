# https://inf-ege.sdamgia.ru/problem?id=27422

# 3 58153
# 7 24923
# 59 2957
# 13 13421
# 149 1171
# 5 34897
# 211 827
# 2 87251

buff = []

for i in range(174457, 174505 + 1):
    if len(buff) == 2:
        print(buff)
        buff.clear()
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            buff.append(j)
        if len(buff) > 2:
            buff.clear()
            break