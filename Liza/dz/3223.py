# Сергей составляет 6-буквенные коды из букв С, О, Л, О, В, Е, Й.
# Буква Й может использоваться в коде не более одного раза, при этом она не может стоять на первом месте,
# на последнем месте и рядом с буквой Е.
# Все остальные буквы могут встречаться произвольное к
# количество раз или не встречаться совсем. Сколько различных кодов может составить Сергей?
import itertools

s = "СОЛОВЕЙ"
a = set(itertools.product(s, repeat=6))
count = 0

for i in a:
    b = "".join(i)
    index = b.find("Й")
    if b.count("Й") == 1 and index != 0 and index != len(b) - 1 and b[index - 1] != "Е" and b[index + 1] != "Е":
        count += 1
    elif b.count("Й") == 0:
        count += 1
print(count)
