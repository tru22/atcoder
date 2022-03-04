N, M = map(int, input().split())

pastas = list(map(int, input().split()))
objectives = list(map(int, input().split()))

flag = True
for i in range(M):
    if objectives[i] in pastas:
        idx = pastas.index(objectives[i])
        pastas.pop(idx)
    else:
        flag = False
        break

if flag == True:
    print("Yes")
else:
    print("No")
