N, W = map(int, input().split())
cheese = [] #おいしさ, 重さ

for i in range(N):
    cheese.append(list(map(int, input().split())))

cheese = sorted(cheese, key = lambda x : x[0], reverse = True)
#print(cheese)

left = W
deliciousness = 0
i = 0
while left > 0 and i < len(cheese):
    if left < cheese[i][1]: #残りの重量だけ載せる
        deliciousness += cheese[i][0] * left
        left = 0
    else: #残重量が現在のチーズ所持重量より大きければ全て載せる
        left -= cheese[i][1]
        deliciousness += cheese[i][0] * cheese[i][1]
    i += 1
    #print(left)

print(deliciousness)
