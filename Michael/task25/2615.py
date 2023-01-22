# Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу.
# Найдите все натуральные числа, принадлежащие отрезку [525784203; 728943762] и имеющие ровно три нетривиальных
# делителя. Для каждого найденного числа запишите в ответе два числа: само число и его наибольший нетривиальный
# делитель. Найденные числа расположите в порядке возрастания.


for i in range(525784203, 728943762 + 1):
    dell = []
    if int(i ** 0.5) ** 2 != i:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            dell.append(j)
            if j != i // j:
                dell.append(i // j)
        if len(dell) > 3:
            break
    if len(dell) == 3:
        print(i, max(dell))