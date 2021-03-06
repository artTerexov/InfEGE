# содержится последовательность целых чисел. Элементы последовательности могут
# принимать целые значения от 0 до 10 000 включительно. Определите количество пар
# чисел, в которых ровно один из двух элементов больше, чем сумма цифр всех чисел в
# файле, делящихся на 35, а шестнадцатеричная запись другого оканчивается на EF. В ответе
# запишите два числа: сначала количество найденных пар, а затем – минимальную сумму элементов
# таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

def hexx(n):
    buff = hex(n)[-2:]
    return buff


with open("files/4722.txt") as f:
    s = f.read().strip().split("\n")

s = [int(i) for i in s]

summ = 0
for i in s:
    if i % 35 == 0:
        for j in str(i):
            summ += int(j)
buff2 = []

for i in range(len(s) - 1):
    if (s[i] > summ >= s[i + 1] and hexx(s[i + 1]) == "ef" and hexx(s[i]) != "ef") \
            or (s[i + 1] > summ >= s[i] and hexx(s[i]) == "ef" and hexx(s[i + 1]) != "ef"):
        buff2.append(s[i] + s[i + 1])

print(len(buff2), min(buff2))
