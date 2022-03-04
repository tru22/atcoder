N, K = map(int, input().split())
numbers = list(map(int, input().split()))
cumsum = [numbers[0]]

for i in range(N - 1):
    cumsum.append(cumsum[i] + numbers[i + 1])

count = 0
for i in range(N):
    for j in range(i + 1):
        if cumsum[i] - cumsum[j] == K:
            count += 1

print(count)
