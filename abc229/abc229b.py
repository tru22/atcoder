A, B = input().split()
length = min(len(A), len(B))
flag = False

for i in range(1, length + 1):
    #print(A[-i], B[-i])
    if int(A[-i]) + int(B[-i]) > 9:
        flag = True

print("Hard" if flag else "Easy")
