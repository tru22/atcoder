jumpNum, objPos = map(int, input().split())
operations = []
for i in range(jumpNum):
    operation = list(map(int, input().split()))
    operations.append(operation)

#print(operations)

flag = False
sums = operations[0]

for i in range(1, len(operations)):
    nextOp = operations[i]
    for j in range(len(sums)):
        #print(len(sums), j)
        currentSum = sums.pop(0)
        for k in range(len(nextOp)):
            if currentSum + nextOp[k] > objPos:
                continue
            sums.append(currentSum + nextOp[k])
    if objPos in sums:
        flag = True
    #print('sums, i: ' + str(sums) + ' ' + str(i))
            
if flag == True:
    print('Yes')
else:
    print('No')
