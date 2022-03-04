targetSentence = input()
baseElements = ['dream', 'dreamer', 'erase', 'eraser']

bfsQueue = [0] #長さを保持するQueue, 切断の開始地点は0番目
flag = False
while len(bfsQueue) != 0:
    t = bfsQueue.pop() #切断の開始地点を更新
    if t == len(targetSentence):
        flag = True
        break
    for element in baseElements:
        if targetSentence[t:t + len(element)] == element:
            bfsQueue.append(t + len(element)) #切断できたらQueueに追加

if flag == True:
    print('YES')
else:
    print('NO')
