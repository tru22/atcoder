N, M = map(int, input().split())
neighbors = [0 for i in range(N)]

flag = True
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    neighbors[u] += 1
    neighbors[v] += 1
    if neighbors[u] > 2 or neighbors[v] > 2:
        flag = False

#print(neighbors)
print("Yes" if flag else "No")
