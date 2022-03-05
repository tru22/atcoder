#get TLE

N = int(input())
mod = 998244353
 
#Xに0は含まれない
#両隣のケタの差の絶対値が1以内 ex. 11, 12, 21
 
numberCounts = [[0 for i in range(9)] for i in range(N)]
numberCounts[0] = [1 for i in range(9)]
 
for i in range(1, N):
    numberCounts[i][0] = numberCounts[i - 1][0] + numberCounts[i - 1][1]
    for j in range(1, 8):
        numberCounts[i][j] = numberCounts[i - 1][j - 1] + numberCounts[i - 1][j] + numberCounts[i - 1][j + 1]
    numberCounts[i][8] = numberCounts[i - 1][7] + numberCounts[i - 1][8]

print(sum(numberCounts[-1]))
