# почему-то в первом ответе на единицу больше

def checkSimple(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


count = []
for l in range(412567, 473266):
    for k in range(2, int(l ** 0.5) + 1):
        if l % k == 0 and k != l // k:
            if checkSimple(k) and checkSimple(l // k):
                count.append(l)
                break


middle = 0
for i in range(len(count)):
    middle += count[i]
middle /= (len(count))

count.append(middle)
count.sort()
middle_index = count.index(middle)
num1 = count[middle_index - 1]
num2 = count[middle_index + 1]

print(len(count) - 1)
if middle - num1 > num2 - middle:
    print(num2)
else:
    print(num1)






