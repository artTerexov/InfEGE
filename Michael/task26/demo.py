# with open('files/demo.txt') as f:
with open('files/5325.txt') as f:
    s = [int(i) for i in f.readlines()]

# удаляем количество коробок
s.pop(0)
# сортируем коробки по убыванию
s.sort(reverse=True)

box = [s[0]]

for i in s:
    if min(box) - i >= 3:
        box.append(i)

print(len(box), min(box))