N = int(input())
graph = []
relations_sum = [0 for i in range(N)]

for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    relations_sum[u] += 1
    relations_sum[v] += 1

flag = False
for relation in relations_sum:
    if relation == N - 1:
        flag = True

print("Yes" if flag else "No")
