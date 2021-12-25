import itertools

a = set(itertools.product("ЯСНОВИДЕЦ", repeat=5))
count = 0
for i in a:
    b = "".join(i)
    if b[0] in "СНВДЦ" and b[-1] in "ЯОИЕ" and b.count(b[0]) == 1 and b.count(b[-1]) == 1:
        count += 1
print(count)
