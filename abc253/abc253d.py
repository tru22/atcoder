N, A, B = map(int, input().split())

summation = N * (N + 1) / 2
mulA = N // A
mulB = N // B
mulAandB = N // (A * B)
sumA = A * mulA * (mulA + 1) / 2
sumB = B * mulB * (mulB + 1) / 2
sumAandB = (A * B) * mulAandB * (mulAandB + 1) / 2

#print(mulA, mulB, mulAandB)
#print(summation, sumA, sumB, sumAandB)
print(int(summation - sumA - sumB + sumAandB))
