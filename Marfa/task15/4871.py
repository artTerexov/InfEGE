# ((x ∈ A) → ¬(x ∈ P)) ∧ (¬(x ∈ Q) → ¬(x ∈ A))

P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
for A in P & Q, P | Q, P ^ Q, P - Q, Q - P:
    flag = True
    for x in range(-1000, 1001):
        F = ((x in A) <= (x not in P)) and ((x not in Q) <= (x not in A))
        if F == 0:
            flag = False
            break
    if flag:
        print(len(A))
        break