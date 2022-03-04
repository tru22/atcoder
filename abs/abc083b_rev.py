#10で割った余りを桁として持ってくる方がかっこいい
#関数定義したほうがいい
N, A, B = map(int, input().split())
numbers = [i + 1 for i in range(N)]

def sumOfDigits(number):
    summation = 0
    while number > 0: #numberが0になるまで割る
        summation += number % 10 #最小桁
        number = number // 10
    return summation

summation = 0
for i in range(len(numbers)):
    sumTmp = sumOfDigits(numbers[i])
    if sumTmp >= A and sumTmp <= B:
        summation += numbers[i]

print(summation)
