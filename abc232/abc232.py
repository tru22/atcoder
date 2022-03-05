import itertools

N, M = map(int, input().split()) #number of balls, ropes
tkBalls = []
aoBalls = []

for i in range(M):
    tkBalls.append(list(map(int, input().split())))

for i in range(M):
    aoBalls.append(list(map(int, input().split())))

#print(tkBalls)
#print(aoBalls)
# 1 - 2, 3, 4, ... N
# initialize, [balls][ropes]
tkList = [[0 for i in range(N)] for j in range(M)]
aoList = [[0 for i in range(N)] for j in range(M)]
for i in range(N):
    tkList[tkBalls[i][0] - 1][tkBalls[i][1] - 1] += 1
    tkList[tkBalls[i][1] - 1][tkBalls[i][0] - 1] += 1
    aoList[aoBalls[i][0] - 1][aoBalls[i][1] - 1] += 1
    aoList[aoBalls[i][1] - 1][aoBalls[i][0] - 1] += 1
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
