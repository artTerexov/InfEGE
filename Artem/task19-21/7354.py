def f(a, c, m):
    if a >= 31 and c != 1:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(a + 1, c + 1, m), f(a + 5, c + 1, m), f(a * 2, c + 1, m)]
    # print(a, c, h)
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


# не забыть поменять второе all на any
result = 0
for i in range(1, 31):
    if f(i, 0, 3):
        result = i
        break
print("Ответ к заданию 19:", result)


# не забыть поменять второе any на all
result = 0
for i in range(1, 31):
    # print(i)
    if f(i, 0, 9):
        result += 1
print("Ответ к заданию 20:", result)


# не забыть поменять второе any на all
result = 0
for i in range(1, 31):
    # print(i)
    if f(i, 0, 6):
        result = i
        break
print("Ответ к заданию 21:", result)