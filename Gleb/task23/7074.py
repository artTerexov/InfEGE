def calc(num, count):
    if count > 12:
        return 0
    buff.add(num)
    count += 1
    return calc(num + 1, count) + calc(num - 1, count)


buff = set()
calc(1, 0)
print()