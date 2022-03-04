# どうしてACなのかわからん…
from collections import defaultdict

N, K = map(int, input().split()) #6, 5
numbers = list(map(int, input().split()))
cumsum = [0]

for i in range(N):
    cumsum.append(cumsum[i] + numbers[i])

#print(numbers)
print(cumsum)
mp = defaultdict(int)
ans = 0
for i in range(1, N + 1):
    mp[cumsum[i - 1]] += 1
    ans += mp[cumsum[i] - K]
    print(mp)
    print(mp[cumsum[i] - K])
    #print(ans)
