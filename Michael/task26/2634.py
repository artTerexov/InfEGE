# 12868


def func(a, n):
    a = sorted(a)
    m = []
    for i in a:
        if sum(m) + i <= n:
            m.append(i)
        else:
            if sum(m) - m[-1] + i <= n:
                m[-1] = i
            else:
                break
    return len(m), max(m)


# Файл
with open("files/2634") as f:
    file = [int(i) for i in f.readlines()]
print('Ответ:', func(file, 12868))

# Тест
with open("files/2634_test") as f:
    file = [int(i) for i in f.readlines()]
print('Тестовый Ответ:', func(file, 100))