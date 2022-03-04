sentence = list(input())[::-1]

flag = False
for i in range(len(sentence) + 1):
    if len(sentence) % 2 == 0 and sentence[0:len(sentence) // 2] == sentence[:len(sentence) // 2 - 1:-1]:
            print('Yes')
            flag = True
            break
    elif len(sentence) % 2 == 1 and sentence[0:len(sentence) // 2] == sentence[:len(sentence) // 2:-1]:
            print('Yes')
            flag = True
            break
    sentence = sentence + ['a']

if flag == False:
    print('No')
