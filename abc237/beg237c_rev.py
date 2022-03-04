sentence = list(input())[::-1]

for i in range(len(sentence) + 1):
    flag = True
    for j in range(len(sentence) // 2):
        if sentence[j] != sentence[-(j + 1)]:
            flag = False
            break
    if flag == True:
        print('Yes')
        break
    sentence.append('a')

if flag == False:
    print('No')
