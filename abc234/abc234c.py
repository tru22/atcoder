#0, 2, 20, 22, 200, 202 -> 二進数?

N = int(input())
N = bin(N)[2:]
print(N.replace('1', '2'))
