sentence = input()
target = "oxx" * (10 ** 5)

#print(target)

flag = False
for i in range(len(target) - len(sentence)):
    #print(target[i:i + len(sentence)])
    if target[i:i + len(sentence)] == sentence:
        flag = True

print("Yes" if flag else "No")
