from collections import defaultdict

N = int(input())
     
names = defaultdict(int)
flag = True
namelist = []
     
for i in range(N):
    first, last = input().split()
    namelist.append([first, last])
    names[first] += 1
    names[last] += 1
     
#print(names)
     
for i in range(N):
    countF = 0
    countL = 0
    first = namelist[i][0]
    last = namelist[i][1]
    #print(first, last)
    for j in range(N):
        #print(namelist[j][0], namelist[j][1])
        if first == namelist[j][0] or first == namelist[j][1]:
            countF += 1
        if last == namelist[j][0] or last == namelist[j][1]:
            countL += 1
    #print(countF, countL)
    if countF > 1 and countL > 1:
        flag = False
        break
     
print("Yes" if flag else "No")
