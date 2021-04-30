# https://inf-ege.sdamgia.ru/problem?id=28677

# ((x → y) ∨ (y ≡ w)) ∧ ((x ∨ z) ≡ w)

print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not x or y) or (y == w)) and ((x or z) == w)
                if F == 1:
                    print(x, y, z, w, F)

# Ответ xyzw

# x y z w
# 0 0 0 0
# 0 0 1 1 подходит
# 0 1 0 0 подходит
# 0 1 1 1
# 1 1 0 1 подходит
# 1 1 1 1
