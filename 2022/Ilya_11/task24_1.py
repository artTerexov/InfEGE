# Текстовыйфайлсостоитнеболеечемиз 10^6 символов X, Y и Z.
# Определите максимальное количество идущих подрядсимволов,
# среди которых каждые два соседних различны. Длявыполненияэтогозаданияследуетнаписатьпрограмму.

with open('24.txt', 'r') as F:
    s = F.read()
count = 1
maximum = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1
    if s[i] == s[i + 1]:
        maximum = max(maximum, count)
        count = 1
print(maximum)

