import itertools

N, M = map(int, input().split()) #number of balls, ropes
tkList = [[0 for i in range(N)] for j in range(N)]
aoList = [[0 for i in range(N)] for j in range(N)]
    
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    tkList[u][v] = tkList[v][u] = 1
        
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    aoList[u][v] = aoList[v][u] = 1
        
#print(tkList)
#print(aoList)

answer = False
for p in itertools.permutations(range(N)):
    flag = True
    for i in range(N):
        for j in range(N):
            if tkList[i][j] != aoList[p[i]][p[j]]:
                flag = False
    if flag:
        answer = True

print("Yes" if answer else "No")
