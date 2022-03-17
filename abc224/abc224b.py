height, width = map(int, input().split())
fields = []

for i in range(height):
    fields.append(list(map(int, input().split())))

flag = True
for i in range(height - 1):
    for j in range(width - 1):
        if fields[i][j] + fields[i + 1][j + 1] > fields[i + 1][j] + fields[i][j + 1]:
            flag = False

print("Yes" if flag else "No")
