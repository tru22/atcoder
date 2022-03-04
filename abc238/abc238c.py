#n桁で，最大9 * 10 ** (n - 1)

N = int(input())
lenNum = len(str(N))
Q = 998244353

def digiSum(num):
    lenNum = len(str(num))
    summation = 0
    for i in range(lenNum - 1):
        end = (9 * 10 ** i) #1~9までの個数の和, 10~99までの個数の和...
        summation +=  end * (end + 1) // 2 #floatにするとえらいことになる

    return summation

summation = digiSum(N)
#print(summation)
end = N - (10 ** (lenNum - 1) - 1)
#print(end)
summation += (end * (end + 1)) // 2
#print(summation)
print(summation % Q)
