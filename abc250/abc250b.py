N, A, B = map(int, input().split())

for i in range(1, N + 1):
    tmpRow = ""
    for j in range(1, N + 1):
        if (i + j) % 2 == 0: # even = print white
            tmpRow += "." * B
            pass
        else: # odd = print black
            tmpRow += "#" * B
            pass
    for k in range(A):
        print(tmpRow)
