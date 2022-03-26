N, P = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(N):
    if nums[i] < P:
        count += 1

print(count)
