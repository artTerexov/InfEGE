import itertools

a = set(itertools.product('СТЕПУХА', repeat=4))
a = list(a)
a.sort()
a = a[1000:]
count = 0

for i in a:
    b = ''.join(i)
    if 'АА' not in b and 'СС' not in b and 'ТТ' not in b and 'УУ' not in b and 'ПП' not in b and 'ХХ' not in b and 'ЕЕ' not in b:
        print(b)
        count += 1
print(count)
