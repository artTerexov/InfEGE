# В текстовом файле k7a-3.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
# Найдите длину самой длинной подцепочки, состоящей из символов A, B, E, F (в произвольном порядке).


with open('k7a-3.txt') as f:
    s = f.read()

count = 0
buff = []
letters = 'ABEF'

for i in s:
    if i in letters:
        count += 1
    else:
        buff.append(count)
        count = 0

print(max(buff))