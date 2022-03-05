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

tkSum = []
aoSum = []
for i in range(N):
    tkSum.append(sum(tkList[i]))
    aoSum.append(sum(aoList[i]))
 
tkSum = tuple(tkSum)
#print(tkSum, aoSum)
 
flag = False
for balls in itertools.permutations(aoSum):
    if balls == tkSum:
        flag = True
 
if flag == True:
    print('Yes')
else:
    print('No')
