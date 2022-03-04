x1, y1, x2, y2 = map(int, input().split())

def getDist(a, b, c, d): #x,y x,y
    return (a - c) ** 2 + (b - d) ** 2

def fiveDist(x, y):
    #距離がsqrt(5)になる点を列挙する
    distList = []

    #x1 +- 2
    for i in range(2):
        for j in range(2):
            dist = [x + ((-1) ** i) * 2, y + ((-1) ** j) * 1]
            distList.append(dist)
    
    #x1 +- 1
    for i in range(2):
        for j in range(2):
            dist = [x + ((-1) ** i) * 1, y + ((-1) ** j) * 2]
            distList.append(dist)

    return distList

"""
print(distList1)
for i in range(len(distList1)):
    print(getDist(x1, y1, distList1[i][0], distList1[i][1]))
"""

distList1 = fiveDist(x1, y1)
distList2 = fiveDist(x2, y2)
flag = False
for d in distList1:
    if d in distList2:
        flag = True

if flag == True:
    print("Yes")
else:
    print("No")
