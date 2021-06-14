# Назовём нетривиальным делителем натурального числа его делитель,
# не равный единице и самому числу. Найдите все натуральные числа, принадлежащие отрезку [12034679; 23175821]
# и имеющие ровно три нетривиальных делителя. Для каждого найденного числа запишите в ответе само число
# и его наибольший нетривиальный делитель. Найденные числа расположите в порядке возрастания.


for i in range(12034679, 23175822):
    d = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            d.append(j)
            if not (i // j in d):
                d.append(i // j)
        if len(d) > 3:
            d.clear()
            break
    if len(d) == 3:
        print(i, max(d))