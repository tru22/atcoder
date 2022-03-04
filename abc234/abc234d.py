N, K = map(int, input().split())
permutation = list(map(int, input().split()))

currentList = permutation[:K - 1]
currentList.sort()
for i in range(N - K + 1):
    sliceIdx = i + K
    print(permutation[:sliceIdx][-K])
