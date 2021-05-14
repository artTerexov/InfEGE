# Сколько чисел длиной 6 можно составить, если известно,
# что цифры идут в порядке убывания, при этом четные и нечетные цифры чередуются?

from itertools import *

s = "1234567890"

a = product(s, repeat=6)

count = 0
for num in a:
    flag = True
    for i in range(0, len(num) - 1):
        if not(num[i] > num[i + 1]
               and ((int(num[i]) % 2 == 0 and int(num[i + 1]) % 2 != 0)
                    or (int(num[i]) % 2 != 0 and int(num[i + 1]) % 2 == 0))):
            flag = False
            break
    if flag:
        count += 1

print(count)


