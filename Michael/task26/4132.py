# Администратор написал скрипт для раскладки N архивов на K дисков, каждый объемом V.
# Алгоритм скрипта обрабатывает файлы в порядке убывания их размера. Если файл помещается на
# диск, то следующий по размеру файл стараются поместить на следующий диск. Если не помещается,
# то на следующий, и так по кругу. Если файл не поместился ни на один диск, то он откладывается в локальную
# папку. Укажите в ответе два числа: объем всех отложенных файлов и их количество

with open("files/test.txt") as f:
    s = f.read().split()

disk_space = int(s[0])
number_of_disks = int(s[1])
number_of_archives = int(s[2])

nums = sorted([int(num) for num in s][3:], reverse=True)

disks = [0 for i in range(number_of_disks)]
local_folder = []

while len(nums) != 0:
    for d in range(len(disks)):
        for num in nums:
            if disks[d] + num <= disk_space:
                disks[d] += num
                nums.pop(0)
            elif d != len(disks)-1:
                break
            elif d == len(disks)-1:
                flag = True
                for k in range(len(disks)):
                    if disks[k] + num <= disk_space:
                        flag = False
                        disks[d] += num
                        nums.pop(0)
                        break
                if flag:
                    local_folder.append(num)
                    nums.pop(0)
                break

print(sum(local_folder), len(local_folder))
