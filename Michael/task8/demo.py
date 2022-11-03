from itertools import permutations, product

# product => комбинации с повторениями
# permutations => комбинации без повторов

a = product('01234567', repeat=5)
count = 0

for i in a:
    el = ''.join(i)
    if el.count('6') == 1 and el[0] != '0':
        j = el.index('6')
        if j == 0 and int(el[j + 1]) % 2 == 0:
            count += 1
        elif j == len(el) - 1 and int(el[j - 1]) % 2 == 0:
            count += 1
        elif int(el[j - 1]) % 2 == 0 and int(el[j + 1]) % 2 == 0:
            count += 1
print(count)
