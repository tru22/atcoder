N, K = map(int, input().split())
numbers = list(map(int, input().split()))

if K == 1:
    print("Yes")
    exit()

numwithidx = []
answer = [0 for i in range(N)]

for i in range(K):
    val = []
    idx = []
    j = i
    while j < N:
        idx.append(j)
        val.append(numbers[j])
        j += K
    numwithidx.append([idx, val])

for nums in numwithidx:
    nums[1] = sorted(nums[1])
    for i in range(len(nums[0])):
        answer[nums[0][i]] = nums[1][i]

for i in range(len(answer) - 1):
    if answer[i] > answer[i + 1]:
        print("No")
        exit()

print("Yes")
