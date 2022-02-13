
a = ["парин", "парун", "пырым"]
c = 'аыеёэияоую'

result = [sum(j in c for j in i) for i in a]

print(result)
