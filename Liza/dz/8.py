# Сергей составляет 6-буквенные коды из букв К, А, Л, И, Й. Буква Й может использоваться в коде не более одного раза,
# при этом она не может стоять на первом месте, на последнем месте и рядом с буквой И.
# Все остальные буквы могут встречаться произвольное количество раз или не встречаться совсем.
# Сколько различных кодов может составить Сергей?

import itertools

a = 'КАЛИЙ'
b = set(itertools.product(a, repeat=6))
buff = []

for i in b:
    c = ''.join(i)
    # flag = 1
    if c[0] != 'Й' and c[-1] != 'Й' and c.count('Й') <= 1 and 'ИЙ' not in c and 'ЙИ' not in c:
        buff.append(c)
        # flag = 0
    # for k in range(1, len(i) - 1):
    #     if i[k] == 'Й' and (i[k - 1] == 'И' or i[k + 1] == 'И'):
    #         flag = 0
    #         break
    # if flag:
    #     buff.append(i)

print(len(buff))

