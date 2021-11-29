# Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв
# и возвращает его же, меняя первую букву на большую.
# Например, print(capitalize('word')) должно печатать слово Word.
#
# На вход подаётся строка, состоящая из слов, разделённых одним пробелом.
# Слова состоят из маленьких латинских букв. Напечатайте исходную строку,
# сделав так, чтобы каждое слово начиналось с большой буквы.
# При этом используйте вашу функцию capitalize().

def capitalize(a):
    s = a.split(' ')
    t = []
    for i in range(0, len(s)):
        l = s[i]
        h = l[0]
        h = ord(h) - 32
        h = chr(h)
        m = l.replace(l[0], h)
        t.append(m)
    print(' '.join(t))

b = input()
capitalize(b)

# harry potter




# def capitalize(a):
#     s = a.split(' ')
#     t = []
#     for i in range(0, len(s)):
#         l = s[i]
#         h = l[0]
#         if ord(h) < 97:
#             h = ord(h) + 32
#             h = chr(h)
#             m = l.replace(a[0], h)
#             k = ' '.join(m)
#         else:
#             h = ord(h) - 32
#             h = chr(h)
#             m = l.replace(a[0], h)
#             k = ' '.join(m)
#         print(k)
#
# b = input()
# capitalize(b)