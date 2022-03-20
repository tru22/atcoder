N = int(input())
points = []

for i in range(N):
    points.append(list(map(int, input().split())))

count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            #print(surface(x1, y1, x2, y2, x3, y3))
            if abs((points[i][0] - points[k][0]) * (points[j][1] - points[k][1]) - (points[j][0] - points[k][0]) * (points[i][1] - points[k][1])) / 2 > 0:
                count += 1

print(count)
