import math

N = int(input())
positions = []

for i in range(N):
    positions.append(list(map(int, input().split())))

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

maximum = 0
for i in range(N):
    cPos = positions[i]
    for j in range(N):
        cDist = dist(cPos[0], cPos[1], positions[j][0], positions[j][1])
        if maximum < cDist:
            maximum = cDist

print(maximum)
