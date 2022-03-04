N, A, B = map(int, input().split())
numbers = [str(i + 1) for i in range(N)]
#print(numbers)

summation = 0
for i in range(len(numbers)):
    sumTmp = 0
    if len(numbers[i]) == 1:
        sumTmp = int(numbers[i][0])
    elif len(numbers[i]) == 2:
        sumTmp = int(numbers[i][0]) + int(numbers[i][1])
    elif len(numbers[i]) == 3:
        sumTmp = int(numbers[i][0]) + int(numbers[i][1]) + int(numbers[i][2])
    elif len(numbers[i]) == 4:
        sumTmp = int(numbers[i][0]) + int(numbers[i][1]) + int(numbers[i][2]) + int(numbers[i][3])
    elif len(numbers[i]) == 5:
        sumTmp = int(numbers[i][0]) + int(numbers[i][1]) + int(numbers[i][2]) + int(numbers[i][3]) + int(numbers[i][4])
    #print(sumTmp)
    if sumTmp >= A and sumTmp <= B:
        summation += int(numbers[i])

print(summation)
