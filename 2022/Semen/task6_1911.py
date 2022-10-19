# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=1911
import itertools
s = "ВАЯЮЩИЙ"
a = set(itertools.product(s, repeat=4))
count = 0
for i in a:
    b = "".join(i)
    if b[0] != "Й" and (b.count("А") + b.count("Я") + b.count("Ю") + b.count("И")) >= 1:
        count += 1
print(count)