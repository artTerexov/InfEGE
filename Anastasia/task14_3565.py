# Некоторое число X из десятичной системы счисления перевели в системы счисления с основаниями 16, 8. Часть символов при записи утеряна. Позиции утерянных символов обозначены символом *:
# X = 3*9 16 = 1** 8 .
# Сколько чисел соответствуют условию задачи?

for i in range(1, 100000):
    x = i
    hexNum = hex(x)[2:]
    octNum = oct(x)[2:]
    if len(hexNum) != 3 and len(octNum) != 3:
        continue
    if hexNum[0] == "3" and hexNum[2] == "9" and len(hexNum) == 3:
        if octNum[0] == "1" and len(octNum) == 3:
            print(x)

# # 10 -> 2
# print(bin(x)[2:])
# # 10 -> 8
# print(oct(x)[2:])
# # 10 -> 16
# print(hex(x)[2:])
