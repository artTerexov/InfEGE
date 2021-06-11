# Вася составляет 5-буквенные коды из букв M, А, Н, О, К.
# Каждую букву нужно использовать ровно 1 раз,
# при этом код не может начинаться с буквы О и не может содержать
# сочетания АО. Сколько различных кодов может составить Вася?
import itertools

a = set(itertools.permutations("МАНОК", r=5))

count = 0

for i in a:
    b = "".join(i)
    if b[0] != "О" and not("АО" in b):
        count += 1
print(count)