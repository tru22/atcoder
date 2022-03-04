import math

N, L, W = map(int, input().split())
startPoints = list(map(int, input().split()))
#startPoints = [0] + startPoints
#startPoints.append(L)

print(N, L, W)
print(startPoints)

coveredSum = 0
for i in range(len(startPoints) - 1):
    if startPoints[i] - startPoints[i] < W:
        coveredSum += startPoints[i + 1] - startPoints[i]
    else:
        coveredSum += W

if L - startPoints[-1] < W:
    coveredSum += L - startPoints[-1]
else:
    coveredSum += W

print(math.ceil((L - coveredSum) / W))
