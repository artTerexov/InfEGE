import math


def average(arr):
    return sum(arr) / len(arr)


def check(num1, num2):
    if (num1 + num2) % 100 == 19 and num1 < digits_average and num2 < digits_average:
        return True
    return False


with open("dz/17-4.txt") as f:
    s = f.read().split()

digits = [int(i) for i in s]
digits_average = average(digits)
digits_pairs = []
minimum = math.inf

for i in range(0, len(digits) - 1):
    if check(digits[i], digits[i + 1]):
        t = (digits[i], digits[i + 1])
        minimum = min(minimum, digits[i] + digits[i + 1])
        digits_pairs.append(t)

print(len(digits_pairs), minimum)

