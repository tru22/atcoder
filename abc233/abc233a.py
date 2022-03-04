import math

X, Y = map(int, input().split())

if X > Y:
    print(0)
else:
    print(math.ceil((Y - X) / 10))
