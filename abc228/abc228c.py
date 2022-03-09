N, K = map(int, input().split())
scores = []

for i in range(N):
    current = list(map(int, input().split()))
    current.append(sum(current))
    scores.append(current)

sortedScores = sorted(scores, key = lambda x : x[3], reverse = True)
#print(scores)

objective = sortedScores[K - 1][3] #sum
for i in range(N):
    if objective - scores[i][3] > 300:
        print("No")
    else:
        print("Yes")
