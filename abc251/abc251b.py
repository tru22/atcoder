from itertools import combinations

N, W = map(int, input().split())
weights = list(map(int, input().split()))

one = weights
two = list(combinations(weights, 2))
three = list(combinations(weights, 3))

two = list(map(sum, two))
three = list(map(sum, three))

answers = set()
for i in one:
    if i <= W:
        answers.add(i)
for j in two:
    if j <= W:
        answers.add(j)
for k in three:
    if k <= W:
        answers.add(k)

print(len(answers))
