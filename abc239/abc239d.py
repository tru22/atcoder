import math

a, b, c, d = map(int, input().split())
tkNums = [i for i in range(a, b + 1)]
aoNums = [i for i in range(c, d + 1)]

def isPrime(num):
    flag = True
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            flag = False
            break

    return flag

#print(tkNums, aoNums)

for num1 in tkNums:
    tkFlag = True
    for num2 in aoNums:
        #print(num1 + num2, isPrime(num1 + num2))
        if isPrime(num1 + num2):
            tkFlag = False
    if tkFlag == True:
        break
    #print("Loop")

if tkFlag:
    print("Takahashi")
else:
    print("Aoki")
