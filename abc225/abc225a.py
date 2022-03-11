import itertools

sentence = list(input())
count = 0
permutations = set()
for i in itertools.permutations(sentence):
    permutations.add(i)

print(len(permutations))
