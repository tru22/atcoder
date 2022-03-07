N, Q = map(int, input().split())
students = list(map(int, input().split()))
students.sort()

def binary_search(dataL, key):
    idxLeft = 0
    idxRight = len(dataL) - 1

    if dataL[0] > key: #最大値 / 最小値超過の場合
        return len(dataL)

    if dataL[-1] < key:
        return 0
    
    while idxLeft <= idxRight:
        idxMid = (idxLeft + idxRight) // 2
        if dataL[idxMid] == key:
            return len(dataL[idxMid:]) #インデックスではなく, key以上の要素の長さとして返す
        elif dataL[idxMid] < key:
            idxLeft = idxMid + 1 #midは含めない
        else:
            idxRight = idxMid - 1 #midは含めない
    #見つからなかった場合
    return len(dataL) - idxLeft

#print(students)
for i in range(Q):
    print(binary_search(students, int(input())))
