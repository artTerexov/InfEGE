# Пользователь вводит произвольное количество слов, каждое из
# которых заканчивается знаком «.». После ввода последнего слова он вводит знак «#».
# Определите, сколько слов начинается и заканчивается на одну и ту же букву.

a = input()
count = 0
while a != "#":
    last = a[-2].lower()
    fist = a[0].lower()
    if last == fist:
        count += 1
    a = input()
print(count)

# a = 5
#
# p = "2356"
#
# leftSum = 0
# rightSum = 0
# for i in range(0, a // 2):
#     leftSum = leftSum + int(p[i])
#     rightSum = rightSum + int(p[i + a // 2])
# print(leftSum, rightSum)
