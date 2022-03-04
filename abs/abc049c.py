import copy

targetSentence = input()
baseElements = ['dream', 'dreamer', 'erase', 'eraser']

def bfs(targetSentence, baseElements):
    targetLen = len(targetSentence)
    elements = copy.deepcopy(baseElements)
    while True:
        sentence = elements.pop(0)    
        if targetSentence == sentence:
            return 'Yes'
        for i in range(len(baseElements)):
            elements.append(sentence + baseElements[i])
        #print(elements)
        #print(min(list(map(len, elements))))
        if min(list(map(len, elements))) > targetLen:
            return 'No'

print(bfs(targetSentence, baseElements))
