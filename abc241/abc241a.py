numbers = list(map(int, input().split()))

current = 0
for i in range(3):
    #print(current)
    current = numbers[current]

print(current)
