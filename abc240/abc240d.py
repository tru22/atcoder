N = int(input())
numbers = list(map(int, input().split()))

stack = []
prev = numbers[0]
continuation = 0

for i in range(N):
    stack.append(numbers[i])
    #print(i, stack)
    
    if prev == numbers[i]:
        continuation += 1
    else:
        continuation = 1

    #print("cont" + str(continuation))
    if continuation == numbers[i]:
        for i in range(continuation):
            stack.pop(-1)
        continuation = 1
        last = stack[-1]
        current = stack[-2]
        i = 1
        while last == current:
            continuation += 1
            current = stack[-2-i]
            i += 1
            
    #print(i, stack)
    prev = numbers[i]
    print(len(stack))
