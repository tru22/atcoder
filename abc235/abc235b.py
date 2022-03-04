N = int(input())
stages = list(map(int, input().split()))

prev = 0
flag = False
for i in range(len(stages)):
    if prev < stages[i]:
        prev = stages[i]
    else:
        break

print(prev)
