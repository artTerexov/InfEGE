# ( (x ∈ A) → (x ∈ P) ) ∧ ( (x ∈ Q) → ¬(x ∈ A) )

P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
a = []


for i in range(1, 31):
    a.append(i)

for x in range(1, 1000):
    F = (not(x in a) or (x in P)) and (not (x in Q) or not (x in a))
    if F == 0:
        a.remove(x)
print(a)
