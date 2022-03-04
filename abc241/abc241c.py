debug = True
N = int(input())

field = []
for i in range(N):
    field.append(list(input()))


flag = False

def check(field, N):
    #ななめ(右下)
    for l in range(N - 6 + 1):
        for k in range(N - 6 + 1): #Nが6だったら1回のチェックで十分
            flag = True
            count = 0
            for i in range(6):
                #print(field[i + l][i + k], end = '')
                if field[i + l][i + k] != "#":
                    count += 1
                if count > 2:
                    flag = False
                    break
            #print()
            if flag == True:
                return True

    #ななめ(右上)
    for l in range(N - 6 + 1):
        for k in range(N - 6 + 1): #Nが6だったら1回のチェックで十分
            flag = True
            count = 0
            for i in range(6):
                #print(field[i + l][i + k], end = '')
                if field[5 - i + l][i + k] != "#":
                    count += 1
                if count > 2:
                    flag = False
                    break
            #print()
            if flag == True:
                return True
    

    #よこ
    for k in range(N): #たてにスライド
        for j in range(N - 6 + 1): #よこにスライド
            flag = True
            count = 0
            for i in range(6): #横に数える
                #print(field[k][i + j], end = '')
                if field[k][i + j] != "#":
                    count += 1
                if count > 2:
                    flag = False
                    break
            #print()
            if flag == True:
                return True
        
    #たて
    for k in range(N): #よこにスライド
        for j in range(N - 6 + 1): #たてにスライド
            flag = True
            count = 0
            for i in range(6): #縦に数える
                #print(field[i + j][k], end = '')
                if field[i + j][k] != "#":
                    count += 1
                if count > 2:
                    flag = False
                    break
            #print()
            if flag == True:
                return True
    

if check(field, N):
    print("Yes")
else:
    print("No")
