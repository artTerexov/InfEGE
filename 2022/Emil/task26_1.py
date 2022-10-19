# № 2644

f = open("26-j2.txt")
# s = f.read().strip()
# f.close()
#
# g = [int(i) for i in s.split("\n")]
#
# numSize = g[0]
#
# g.pop(0)
#
# g = sorted(g)
#
# middle = sum(g) / numSize
# median = g[numSize // 2]
# count = 0
#
# for i in g:
#     if middle <= i <= median:
#         count += 1
#
# print(count)

s = f.read().strip()
array = [int(number) for number in s.split('\n')]
f.close()

array.pop(0)

length = len(array)

median = sorted(array)
median = median[length // 2]
average = sum(array) / length
count = 0

for i in array:
    if average <= i <= median:
        count += 1

print(count)
