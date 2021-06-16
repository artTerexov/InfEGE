s = '2' * 8 + '1' * 25

while ('11' in s) or ('112' in s):
    if '112' in s:
        s = s.replace('112', '5', 1)
    else:
        s = s.replace('11', '7', 1)
summa = 0
print(s)
for i in s:
    summa += int(i)
print(summa)