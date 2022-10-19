import itertools

s = "ШКОЛА"
a = set(itertools.product(s, repeat=5))
count = 0

for i in a:
    b = "".join(i)
    if (b.count("О") + b.count("А")) >= 1:
        count += 1
print(count)