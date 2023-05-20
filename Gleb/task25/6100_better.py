buff = []

# * - пустота (1?1?1?11)
for x1 in range(10):
    for x2 in range(10):
        for x3 in range(10):
            number = int('1' + str(x1) + '1' + str(x2) + '1' + str(x3) + '1' + '1')
            result = 0
            for i in str(number):
                result += int(i)
            if number <= 10 ** 10 and number % 2023 == 0 and result == 22:
                buff.append([number, number // 2023])



# * - 1 символ (1?1?1?1*1)
for y in range(10):
    for x1 in range(10):
        for x2 in range(10):
            for x3 in range(10):
                number = int('1' + str(x1) + '1' + str(x2) + '1' + str(x3) + '1' + str(y) + '1')
                result = 0
                for i in str(number):
                    result += int(i)
                if number <= 10 ** 10 and number % 2023 == 0 and result == 22:
                    buff.append([number, number // 2023])

# * - 2 символ (1?1?1?1**1)
for y1 in range(10):
    for y2 in range(10):
        for x1 in range(10):
            for x2 in range(10):
                for x3 in range(10):
                    number = int('1' + str(x1) + '1' + str(x2) + '1' + str(x3) + '1' + str(y1) + str(y2) + '1')
                    result = 0
                    for i in str(number):
                        result += int(i)
                    if number <= 10 ** 10 and number % 2023 == 0 and result == 22:
                        buff.append([number, number // 2023])

buff.sort()
print(buff)


# 19131511 9457
# 1012141291 500317
# 1319111311 652057
# 1516111051 749437