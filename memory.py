import psutil

virtual_memory = psutil.virtual_memory()
index = 0
print(type(virtual_memory))
for i in virtual_memory:
    memory = i / 2 ** 20
    array = ['Всего', 'Доступно',
             'Проценты', 'Используемое', 'Свободное',
             'Активное', 'Неактивное', 'Wired']
    if index != 2:
        print(f'{memory:.2f} Мб - {array[index]}')
    index += 1

print(f'{virtual_memory[2]}% Проценты')

