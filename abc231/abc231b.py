from collections import defaultdict

namesDict = defaultdict(int)
N = int(input())
for i in range(N):
    namesDict[input()] += 1

namesDict = sorted(namesDict.items(), key = lambda x : x[1], reverse = True) #リストに変換してソート1
#print(namesDict)
topname = namesDict[0][0]
print(topname)
