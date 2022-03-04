#BA -> BBB -> AB
#BB -> A
#AB ->
#AA

N = int(input())
target = input()


flag = True
while flag == True:
    #print(target)
    flag = False
    i = 0
    targetSize = len(target)
    while i < targetSize - 1:
        if target[i] + target[i + 1] == "BA":
            flag = True
            target = target[:i] + "AB" + target[i + 1 + 1:]
            targetSize = len(target)
            continue
        if target[i] + target[i + 1] == "BB":
            flag = True
            target = target[:i] + "A" + target[i + 1 + 1:]
            targetSize = len(target)
            continue
        i += 1

print(target)
