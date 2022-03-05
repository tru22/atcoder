N = int(input())
Q = 998244353

#Xに0は含まれない
#両隣のケタの差の絶対値が1以内 ex. 11, 12, 21

numbers = [str(i) for i in range(1, 10)]
#print(numbers)

for i in range(N - 1):
    newNumbers = []
    for j in range(len(numbers)):
        num = numbers[j][-1]
        #print(num)
        if int(num) > 1:
            newNumbers.append(numbers[j] + str(int(num) - 1))
        if int(num) < 9:
            newNumbers.append(numbers[j] + str(int(num) + 1))
        newNumbers.append(numbers[j] + num)
    numbers = newNumbers
    #print(numbers)

print(numbers)
print(len(numbers) % Q)
