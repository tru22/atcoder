N = int(input())
Q = 998244353

def func(num): #f(x)
    lenNum = len(str(num))
    end = num - (10 ** (lenNum - 1) - 1)
    result = end * (end + 1) / 2

    return result

print(func(N))
