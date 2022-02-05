# Тройка идущих подряд чисел последовательности называется уникальной,
# если только второе из них является положительным трёхзначным нечётным числом.
# Определите количество уникальных троек чисел, а затем – максимальную из всех сумм таких троек.
with open('17-199.txt') as f:
    s = f.read().strip().split('\n')
s = [int(i) for i in s]
buff = []
for i in range(0, len(s) - 2):
    nums = [s[i], s[i + 1], s[i + 2]]
    if (nums[1] % 2 != 0) and (nums[1] >= 100) and (nums[1] <= 999):
        if not ((nums[0] % 2 != 0) and (nums[0] >= 100) and (nums[0] <= 999)):
            if not ((nums[2] % 2 != 0) and (nums[2] >= 100) and (nums[2] <= 999)):
                buff.append(sum(nums))
print(len(buff), max(buff))
