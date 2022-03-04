a, b = map(int, input().split())

def Neighbor(num):
    numNeighbor = [num - 1, num + 1]
    if num == 1:
        numNeighbor[0] = 10
    elif num == 10:
        numNeighbor[1] = 1

    return numNeighbor

aNeighbor = Neighbor(a)
#print(aNeighbor)

if b in aNeighbor:
    print("Yes")
else:
    print("No")
