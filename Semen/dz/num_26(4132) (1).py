# Алгоритм скрипта обрабатывает файлы в порядке убывания их размера. Если файл помещается на диск, то следующий по размеру файл стараются поместить на следующий диск.
# Если не помещается, то на следующий, и так по кругу.
# Если файл не поместился ни на один диск, то он откладывается в локальную папку. Укажите в ответе два числа: объем всех отложенных файлов и их количество

with open("4132.txt") as f:
    s = [int(i) for i in f.read().strip().split()]

limit = s[0]
disk = s[1]

s = s[3:]
s.sort(reverse=True)

a = [[] for i in range(disk)]
b = []

count = 0
n = 0
for i in s:
    if sum(a[count]) + i <= limit:
        a[count].append(i)
        count += 1
    else:
        c = count
        count += 1
        while count != c:
            if sum(a[count]) + i <= limit:
                a[count].append(i)
                break
            else:
                n += 1
            if n == 7:
                b.append(i)
            count += 1
            if count == 8:
                count = 0
        if count == c:
            b.append(i)
        count += 1
    if count == 8:
        count = 0

print(sum(b), len(b))