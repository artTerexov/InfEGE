# Дано действительное положительное число a и целоe число n.
# Вычислите a ** n. Решение оформите в виде функции power(a, n).

def power(a, n):
    res = 1
    if n > 0:
        k = n
        while k != 0:
            res = res * a
            k -= 1
        print(res)
    else:
        k = n
        while k != 0:
            res = res * a
            k += 1
        h = 1 / res
        print(h)


a = float(input())
n = float(input())

print(power(a, n))
