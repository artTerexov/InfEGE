import itertools
b = []
for i in range(0, 204):
    s = '1' * i + '2' + '1' * (203 - i)
    l = s
    while "111" in s or "222" in s:
        if "111" in s:
            s = s.replace("111", "22", 1)
        else:
            s = s.replace("222", "11", 1)
    b.append((len(s), s, l))
print(max(b))