# pip install psutil
import psutil


# Количество ядер
print(f'Физические ядра: {psutil.cpu_count(logical=False)}')
print(f'Всего ядер: {psutil.cpu_count(logical=True)}')


# Частота процессора
cpu_frequency = psutil.cpu_freq()
print(f'Максимальная частота: {cpu_frequency.max}MHZ')
print(f'Минимальная частота: {cpu_frequency.min}MHZ')
print(f'Текущая частота: {cpu_frequency.current}MHZ')


# Использование процессора
print('Использование процессора каждым ядром:')
for number, percent in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f'Ядро {number}: {percent}%')

print(f'Итоговое использование процессора: {psutil.cpu_percent()}%')
