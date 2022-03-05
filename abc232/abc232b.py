sentence = list(input())
target = input()

#0 < K < 26
#ord('a') = 97, ord('z') = 122
#chr(97) = 'a'
flag = False
for i in range(26 + 1):
    K = i
    newSentence = ""
    for j in range(len(sentence)):
        newSentence += chr((ord(sentence[j]) -97 + K) % 26 + 97)
    if newSentence == target:
        flag = True

if flag == True:
    print("Yes")
else:
    print("No")
