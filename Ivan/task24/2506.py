# В текстовом файле k7.txt находится цепочка из символов латинского алфавита A, B, C
# длиной не более 10^6 символов. Найдите длину самой длинной подцепочки, состоящей из символов C.

with open('files/k7.txt') as f:
    s = f.read()


count = 0
maxCount = 0
for i in s:
    if i == "C":
        count += 1
    else:
        if maxCount < count:
            maxCount = count
        count = 0

print(maxCount)