# (№ 2506) В текстовом файле k7.txt находится цепочка из символов латинского алфавита A, B, C
# длиной не более 106 символов. Найдите длину самой длинной подцепочки, состоящей из символов C.


with open("files/2506.txt") as f:
    s = f.read()

count = 0
maximum = 0

for i in s:
    if i == "C":
        count += 1
    else:
        maximum = max(count, maximum)
        count = 0

print(maximum)