import math

n = int(input())

if n * math.log2(2) > 2 * math.log2(n):
    print("Yes")
else:
    print("No")
