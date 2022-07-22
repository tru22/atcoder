n, x, y, z = map(int, input().split())
math_scores = list(map(int, input().split()))
eng_scores = list(map(int, input().split()))
eng_and_math_scores = [i + j for i, j in zip(math_scores, eng_scores)]

for i in range(len(math_scores)):
    math_scores[i] = (math_scores[i], i)
    eng_scores[i] = (eng_scores[i], i)
    eng_and_math_scores[i] = (eng_and_math_scores[i], i)

math_scores = sorted(math_scores, key = lambda x : x[0], reverse = True)
eng_scores = sorted(eng_scores, key = lambda x : x[0], reverse = True)
eng_and_math_scores = sorted(eng_and_math_scores, key = lambda x : x[0], reverse = True)

"""
print(math_scores)
print(eng_scores)
print(eng_and_math_scores)
"""

# process X
not_passed = set([i for i in range(n)])
for i in range(x):
    if math_scores[i][1] in not_passed:
        not_passed.remove(math_scores[i][1])

# process Y
i = 0
j = 0
while j < y and i < n:
    if eng_scores[i][1] in not_passed:
        not_passed.remove(eng_scores[i][1])
        j += 1
        i += 1
    else:
        i += 1
        continue

# process Z
i = 0
j = 0
while j < z and i < n:
    if eng_and_math_scores[i][1] in not_passed:
        not_passed.remove(eng_and_math_scores[i][1])
        j += 1
        i += 1
    else:
        i += 1
        continue

not_passed = list(not_passed)
not_passed = map(lambda x : x + 1, not_passed)
passed = set([i + 1 for i in range(n)]) - set(not_passed)
passed = sorted(list(passed))
for i in passed:
    print(i)
