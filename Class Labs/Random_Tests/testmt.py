M = [3,4]
L = []
for x in range(10,600):
    for n in M:
        if x % n != 0:
            break
    else:
        print('it happen')
        L.append(x)

print(L)


