# Программа для двух куч
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=2387

def f(a, b, c, m, f1, f2):
    if a + b >= 45:
        return f2(c, m)
    if c == m:
        return 0
    h = [f(a, b + 1, c + 1, m, f1, f2), f(a + 1, b, c + 1, m, f1, f2),
         f(a, b * 3, c + 1, m, f1, f2), f(a * 3, b, c + 1, m, f1, f2)]
    return any(h) if (c + 1) % 2 == m % 2 else f1(h)


print("Программа для решение теории игр")




for b in range(1, 41):
    if f(4, b, 0, 2, any, (lambda x, y: x == y)) == 1:
        print("№ 19 ->", b)
        break
print("№ 20 ->", end=" ")
for b in range(1, 41):
    if f(4, b, 0, 3, all, (lambda x, y: x == y)) == 1:
        print(b, end=" ")
print()

print("№ 21 ->", end=" ")
for b in range(1, 41):
    if f(4, b, 0, 4, all, (lambda x, y: x % 2 == y % 2)) == 1:
        print(b, end=" ")
print()


# m = 2 -> Победа первым ходом Ваня -> 19 задание
# m = 3 -> Победа вторым ходом Пети -> 20 задание
# m = 4 -> Победа вторым ходом Вани -> 21 задание