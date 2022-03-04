from collections import defaultdict

N, Q = map(int, input().split())
numbers = list(map(int, input().split()))


queries = []
queryDic = defaultdict(list) #存在しない場合, list()を返す = []を返す
for i in range(N):
    queryDic[numbers[i]].append(i + 1)

for i in range(Q):
    key, order = map(int, input().split())
    if order > len(queryDic[key]):
        print(-1)
    else:
        print(queryDic[key][order - 1])
