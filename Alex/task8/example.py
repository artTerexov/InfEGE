from itertools import product, permutations

# А Б В
# Сколько комбинаций длинны 4 мы можем составить

# a = product('АБВ', repeat=4)
#
# for i in a:
#     b = ''.join(i)


# А Б В Г
# Сколько комбинаций длинны 4 мы можем составить, причем буквы не повторяются

# a = permutations('АБВГ', r=4)
#
# for i in a:
#     b = ''.join(i)
#     print(b)

# подлодка
# Леша составил комбинации перестановкой слова ПОДЛОДКА

# a = set(permutations('ПОДЛОДКА', r=8))
# count = 0
# for i in a:
#     b = ''.join(i)
#     count += 1
#     print(b)
# print(count)