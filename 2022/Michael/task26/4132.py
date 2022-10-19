# Администратор написал скрипт для раскладки N архивов на K дисков, каждый объемом V.
# Алгоритм скрипта обрабатывает файлы в порядке убывания их размера. Если файл помещается на
# диск, то следующий по размеру файл стараются поместить на следующий диск. Если не помещается,
# то на следующий, и так по кругу. Если файл не поместился ни на один диск, то он откладывается в локальную
# папку. Укажите в ответе два числа: объем всех отложенных файлов и их количество

with open("files/4132.txt") as f:
    s = f.read().split()

disk_space = int(s[0])
number_of_disks = int(s[1])
number_of_archives = int(s[2])

nums = sorted([int(num) for num in s][3:], reverse=True)

disks = [0 for i in range(number_of_disks)]
local_folder = []
d = 0
c = -1

for num in nums:
    while True:
        if disks[d % number_of_disks] + num <= disk_space:
            disks[d % number_of_disks] += num
            d += 1
            c = -1
            break
        elif c == -1:
            c = d % number_of_disks
        elif d % number_of_disks == c:
            local_folder.append(num)
            c = -1
            d = 0
            break
        d += 1

print(sum(local_folder), len(local_folder))
