height, width = map(int, input().split())

matrix = []
for i in range(height):
    matrix.append(list(map(int, input().split())))

for i in range(width):
    for j in range(height):
        if j == height - 1:
            print(matrix[j][i])
        else:
            print(matrix[j][i], end=' ')
