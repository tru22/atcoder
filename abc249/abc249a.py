A, B, C, D, E, F, X = map(int, input().split())

left = X
tk = 0
ao = 0
while left > 0:
    if left > A:
        tk += A * B
        left -= A
    else:
        tk += left * B
        left = 0
    if left > C:
        left -= C
    else:
        left = 0

left = X
while left > 0:
    if left > D:
        ao += D * E
        left -= D
    else:
        ao += left * E
        left = 0
    if left > F:
        left -= F
    else:
        left = 0

#print(tk, ao)
if tk > ao:
    print("Takahashi")
elif tk < ao:
    print("Aoki")
else:
    print("Draw")
