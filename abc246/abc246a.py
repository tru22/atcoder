x = []
y = []

for i in range(3):
    xtmp, ytmp = map(int, input().split())
    x.append(xtmp)
    y.append(ytmp)

for i in x:
    if x.count(i) == 2:
        continue
    else:
        print(i, end=' ')

for i in y:
    if y.count(i) == 2:
        continue
    else:
        print(i)
