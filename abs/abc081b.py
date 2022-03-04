N = int(input())
numbers = list(map(int, input().split()))

processTimes = 0
while True:
    if sum([i % 2 for i in numbers]) != 0:
        break
    else:
        numbers = [i // 2 for i in numbers]
        processTimes += 1

print(processTimes)
