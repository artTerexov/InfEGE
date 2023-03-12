# (((X & 13 ≠ 0) ∨ (X & 39 = 0)) → (X & 13 ≠ 0)) ∨ ((X & A = 0) ∧ (X & 13 = 0))


for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        if ((((x & 13 != 0) or (x & 39 == 0)) <= (x & 13 != 0)) or ((x & A == 0) and (x & 13 == 0))) != 1:
            flag = False
            break
    if flag == True:
        print(A)