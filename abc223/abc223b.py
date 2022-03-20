sentence = input()
shifted = []
for i in range(len(sentence)):
    shifted.append(sentence[i:] + sentence[:i])

shifted.sort()

print(shifted[0])
print(shifted[-1])
