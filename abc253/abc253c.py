import bisect
from collections import defaultdict

Q = int(input())
s = defaultdict(int)
numbers = []
     
for i in range(Q):
    query = input().split()
    if len(query) == 1: # max-min
        print(numbers[-1] - numbers[0])
        
    elif len(query) == 2: # append
        x = int(query[1])
        s[x] += 1
        bisect.insort(numbers, x)
        
    elif len(query) == 3: # delete
        x, c = int(query[1]), int(query[2])
        if c >= s[x]:
            for j in range(s[x]):
                del numbers[bisect.bisect_left(numbers, x)]
            s.pop(x)
        else:
            for j in range(c):
                del numbers[bisect.bisect_left(numbers, x)]
            s[x] -= c

    #print(s, numbers)
