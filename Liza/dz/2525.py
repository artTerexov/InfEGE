# Текстовый файл 24-1.txt состоит не более чем из 106 символов - заглавных латинских букв и цифр.
# Определите максимальное чётное число, записанное в этом файле.
# Под числом подразумевается последовательность цифр, ограниченная другими символами (не цифрами).


with open('24-1.txt') as f:
    s = f.read()

buff = []
numbers = '1234567890'
num = ''

for i in range(len(s) - 1):
    if s[i] in numbers and s[i + 1] in numbers:
        num += str(s[i])
    if s[i] in numbers and s[i + 1] not in numbers:
        num += str(s[i])
        num = int(num)
        if num % 2 == 0:
            buff.append(num)
        num = ''

print(max(buff))