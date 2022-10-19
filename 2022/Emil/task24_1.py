# Текстовый файл состоит не более чем из 10^6 символов L, D и R.
# Определите максимальную длину цепочки вида LDRLDRLDRLDL... (составленной из фрагментов
# LDR, последний фрагмент может быть неполным).
# Для выполнения этого задания следует написать программу. Ниже приведён
# файл, который необходимо обработать с помощью данного алгоритма.

f = open("zadanie24_2.txt")
s = f.read()
f.close()

count = 0
maximum = 0

for i in s:
    if (i == "L" and count % 3 == 0) or (i == "D" and count % 3 == 1) or (i == "R" and count % 3 == 2):
        count += 1
    else:
        maximum = max(maximum, count)
        if i == "L":
            count = 1
        else:
            count = 0
print(maximum)