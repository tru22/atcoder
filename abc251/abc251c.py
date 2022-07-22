from collections import defaultdict

N = int(input())

originals = defaultdict(int)
maxIdx = 0
maxVal = 0

for i in range(N):
    s, t = input().split()
    t = int(t)
    #print(s, t, originals)
    if originals[s] != 1 and t > maxVal:
        maxIdx = i
        maxVal = t
    #print(maxIdx)
    originals[s] = 1

print(maxIdx + 1)
