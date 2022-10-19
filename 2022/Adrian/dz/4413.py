a = (5 ** 300 * 15 ** 100) - (25 ** 50 + 125 ** 100)
sis = 5

ost = ''
while a > 0:
	ost += str(a % sis)
	a = a // sis

s = 0
for i in ost:
	if i != '4':
		s += int(i)
print(s)