a = 'АКАРИДА'
# АИ     РДК
for j in range(len(a) - 1):
    if a[j] in 'АИ' and a[j + 1] in 'АИ':
        print('OK')
    if a[j] in 'КРД' and a[j + 1] in 'КРД':
        print('ОККК')



