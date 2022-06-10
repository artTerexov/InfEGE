d = open('26-84.txt').readline().split(' ')
f = open('26-84b.txt').read().split(' ')
h = [int(x) for x in f]
g = [int(x) for x in d]
kol_AUD = 100000
kol_STUD = h
kol_MEST_V_AUD = g
min_AUD = min(g)
min_kol_STUD = min(kol_STUD)
count = 0
for i in kol_MEST_V_AUD:
    if i <= min_kol_STUD:
        count += 1
print(count)
