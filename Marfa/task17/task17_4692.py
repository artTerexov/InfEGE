# Элементы последовательности могут принимать целые значения от 0 до 10 000 включительно.
# Определите количество пар чисел, в которых хотя бы один из двух элементов больше, чем наибольшее
# из всех чисел в файле, делящихся на 111, и хотя бы один элемент из двух оканчивается на 7.
# В ответе запишите два числа: сначала количество найденных пар, а затем – минимальную сумму элементов
# таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.


with open("files/4692.txt") as f:
    s = f.read().strip().split("\n")

s = [int(i) for i in s]