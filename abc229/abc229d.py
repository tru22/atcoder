S = input()
K = int(input())

csum = [0]
#ピリオドの出現回数の累積和を取る
for i in range(1, len(S) + 1):
    if S[i - 1] == '.':
        csum.append(csum[i - 1] + 1)
    else:
        csum.append(csum[i - 1])

#print(S)
#print(csum)

maximum = 0
left = 0
right = 1 #半開区間
for left in range(len(S)):
    #条件を満たせばrightをインクリメント
    #区間内の.の出現回数がK以下であればOK
    #right - leftが過去のmaxより大きければ更新
    #print("left, right", left, right)
    while right < len(S) and csum[right + 1] - csum[left] <= 2:
        #print("left, right", left, right)
        right += 1
    #print("left, updated right", left, right)
    maximum = max(maximum, len(S[left:right]))
    if right == left: #次のleftに行く前に更新
        right += 1

print(maximum)
