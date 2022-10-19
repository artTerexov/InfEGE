s = 9 ** 81 + 27 ** 729 - 4
sis = 9

ost = ''
while s > 0:
	ost += str(s % sis)
	s = s // sis
ost = ost.replace('0', '8')
print(ost.count('8'))
