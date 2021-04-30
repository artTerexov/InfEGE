# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов X.
# Хотя бы один символ X находится в последовательности.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

s = open("24_demo (1).txt").read()

count = 0
buffer = 0

for i in range(0, len(s)):
    if s[i] == "X":
        count += 1
    else:
        buffer = max(buffer, count)
        count = 0
print(buffer)
