S = input()
K = int(input())

csum = [0]
#ピリオドの出現回数の累積和を取る
for i in range(0, len(S)):
    if S[i] == '.':
        csum.append(csum[i] + 1)
    else:
        csum.append(csum[i])

#print(S)
#nprint(csum)
#print(csum[5] - csum[0])

maximum = 0
left = 0
right = 0 #半開区間
for left in range(len(S)):
    #条件を満たせばrightをインクリメント
    #区間内の.の出現回数がK以下であればOK
    #right - leftが過去のmaxより大きければ更新
    #print("left, right", left, right)
    while right < len(S) and csum[right + 1] - csum[left] <= K:
        #print("left, right", left, right)
        right += 1
    #print("left, updated right", left, right)
    maximum = max(maximum, right - left)

print(maximum)
