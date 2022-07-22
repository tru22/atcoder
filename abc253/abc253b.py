H, W = map(int, input().split())

field = []
for i in range(H):
    field.append(input())

positions = []
for i in range(H):
    for j in range(W):
        if field[i][j] == "o":
            positions.append([i, j])

distance = abs(positions[0][0] - positions[1][0]) + abs(positions[0][1] - positions[1][1])
print(distance)
