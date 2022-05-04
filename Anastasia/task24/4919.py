# Текстовый файл 24-191.txt содержит строку из заглавных латинских букв,
# всего не более чем из 106 символов. Определите количество подстрок длиной не менее 20 символов,
# которые начинаются буквой A, содержат ровно две буквы F, заканчиваются буквой B и не содержат других букв A и B,
# кроме первой и последней.
with open('files/4919.txt') as f:
    s = f.read()
# s = 'ADFFJKJJKGHJKJKJURUB'
count = 0
big = 0
two = 0
print('len F A B')
for i in range(len(s)):
    if s[i] == 'A':
        indexB = s.find('B', i)
        if indexB - i >= 19 and s.count('A', i + 1, indexB) == 0 and s.count('F', i + 1, indexB) == 2:
            test = s[i:indexB + 1]
            count += 1
print(count)


# Два способа пробега по строке
# test = 'Anastasia'
# 1 способ - По индексам
# for i in range(len(test)):
#     print(test[i])
# 2 способ - По символам
# for i in test:
#     print(i)
