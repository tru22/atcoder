N, M = map(int, input().split())

#i, j は (i - 1) * 7 + j
#左端(j = 0)なら(i - 1) * 7
flag = True
target = []
for i in range(N):
    current = list(map(int, input().split()))
    target.append(current)

first = target[0][0]
answer = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(first + 7 * i + j)
    answer.append(row)

#print(target, answer)

for i in range(N):
    for j in range(M):
        if answer[i][j] != target[i][j]:
            flag = False
    
print("Yes" if flag else "No")
