d = open('files/26-59.txt').readlines()
d.pop(0)
d = [(int(i.split()[0]), int(i.split()[1])) for i in d]
d.sort()
print()