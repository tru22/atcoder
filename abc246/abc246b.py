import math

A, B = map(int, input().split())
dist = math.sqrt(A ** 2 + B ** 2)
print(A / dist, B / dist)
