N = int(input())

total = []
for i in range(1, N + 1):
    current = []
    for j in range(1, i + 1):
        if j == 1 or j == i:
            current.append(str(1))
        else:
            current.append(str(int(total[i - 2][j - 2]) + int(total[i - 2][j - 1])))
    total.append(current)
    print(" ".join(current))
