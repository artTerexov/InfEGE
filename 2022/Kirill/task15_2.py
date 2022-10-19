# ((x ∈ P) → (x ∈ A)) ∨ (¬(x ∈ A) → ¬(x ∈ Q))
P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
A = []


for x in range(-100, 100):
    if (x in P) and (x in Q):
        A.append(x)
print(A)