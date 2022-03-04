from collections import defaultdict

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
cumsum = [0]

for i in range(N):
    cumsum.append(cumsum[i] + numbers[i])

print(numbers)
print(cumsum)
mp = defaultdict(int)
for i in range(0, N + 1):
    mp[cumsum[i]] += 1

print(mp)
