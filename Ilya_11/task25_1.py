import time
start_time = time.time()

for i in range(174457, 1745050+1):
    Del = []                    # Обнуляющийся список делителей
    for d in range(2, int(i ** 0.5) + 1):        # Проверяю все нетривиальные делители
        if i % d == 0:            # Проверка на делимость
            Del.append(d)         # Добавляю в список
            if not(i // d in Del):
                Del.append(i // d)
        if len(Del) > 2:        # Если более 2-ух делителей
            break               # Перехожу к следующему числу
    if len(Del) == 2: # Если нашлось всего 2 делителя
        print(*Del)             # Список выводится с новой строки

print("--- %s seconds ---" % (time.time() - start_time))