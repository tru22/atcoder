N = int(input())
undeclared = [i for i in range(1, 2 * N + 1 + 1)]
declared = []

print(1) # 1は最初に宣言する
undeclared.pop(1 - 1)

while True:
    aoki = int(input())
    if aoki == 0:
        break
    undeclared.pop(undeclared.index(aoki))
    print(undeclared[0])
    undeclared.pop(0)
    #print(undeclared)
