rowNum = int(input())
testcases = []
for i in range(rowNum):
    testcaseTmp = list(map(int, input().split()))
    testcases.append(testcaseTmp) #a, s

#print(testcases)

for i in range(len(testcases)):
    a = testcases[i][0]
    s = testcases[i][1]
    x = s
    y = 0
    flag = False
    for j in range(testcases[i][1]):
        x = s - y
        #print('j: ' + str(j))
        #print('x: ' + str(x))
        #print('y: ' + str(y))
        if bin(x) and bin(y) == bin(a):
            print('Yes')
            flag = True
            break
        y += 1
    if flag == False:
        print('No')
