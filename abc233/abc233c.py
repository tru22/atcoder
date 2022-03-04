N, X = map(int, input().split())

balls = list(map(int, input().split()))[1:]
for i in range(N - 1):
    newBalls = list(map(int, input().split()))[1:]
    nextBalls = []
    for j in range(len(balls)):
        for k in range(len(newBalls)):
            nextBalls.append(balls[j] * newBalls[k])
    balls = nextBalls

print(balls.count(X))
