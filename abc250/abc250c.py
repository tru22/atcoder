N, Q = map(int, input().split())
balls = [i + 1 for i in range(N)]
idxDict = {i + 1: i for i in range(N)} # ball value(key), position idx(value)

for i in range(Q):
    instruction = int(input())
    idx = idxDict[instruction]
    #print(idx)
    if idx == N - 1: # if its end
        current = balls[idx]
        target = balls[idx - 1]
        
        balls[idx - 1] = balls[idx]
        balls[idx] = target
        idxDict[target] += 1
        idxDict[current] -= 1
    else:
        current = balls[idx]
        target = balls[idx + 1]
        
        balls[idx + 1] = balls[idx]
        balls[idx] = target
        idxDict[target] -= 1
        idxDict[current] += 1
    #print(balls)

print(" ".join(list(map(str, balls))))
