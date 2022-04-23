from collections import defaultdict
from itertools import combinations

N, K = map(int, input().split())
strings = []

for i in range(N):
    strings.append(input())

maximum = 0
for i in range(N):
    comblist = list(combinations(strings, i + 1))
    #print(comblist)
    for c in comblist:
        count = defaultdict(int)
        for k in range(len(c)):
            string = c[k]
            for j in range(len(string)):
                count[string[j]] += 1

        summation = 0
        #print(count.items())
        for j in count.items():
            if j[1] == K:
                summation += 1
        #print(summation)
        if summation > maximum:
            maximum = summation

print(maximum)
