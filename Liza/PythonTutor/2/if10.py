# Шахматный конь ходит буквой “Г” — на две клетки
# по вертикали в любом направлении и на одну клетку
# по горизонтали, или наоборот. Даны две различные
# клетки шахматной доски, определите, может ли
# конь попасть с первой клетки на вторую одним ходом.

# где-то тут есть ошибка, так как тест с 2 4 3 2 не получается

sx = int(input())
nx = int(input())
sz = int(input())
nz = int(input())

if (sx + 2 == sz) and (nx + 1 == nz):
    print('YES')
elif (sx + 2 == sz) and (nx - 1 == nz):
    print('YES')
elif (sx - 2 == sz) and (nx + 1 == nz):
    print('YES')
elif (sx - 2 == sz) and (nx - 1 == nz):
    print('YES')
elif (nx + 2 == nz) and (sx + 1 == nz):
    print('YES')
elif (nx + 2 == nz) and (sx - 1 == sz):
    print('YES')
elif (nx - 2 == nz) and (sx + 1 == sz):
    print('YES')
elif (nx - 2 == nz) and (sx - 1 == sz):
    print('YES')
else:
    print('NO')