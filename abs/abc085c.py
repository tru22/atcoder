#制約条件を上手く使うと，forを三重ループにしなくて済む
bills, totalAmount = map(int, input().split())
bills = bills + 1


flag = False
for i in range(bills):
    for j in range(bills - i):
        k = bills -1 - i - j
        summation = 1000 * i + 5000 * j + 10000 * k
        if summation == totalAmount:
            answer = '{0} {1} {2}'.format(k, j, i)
            #print(answer)
            flag = True

if flag == False:
    print('-1 -1 -1')
else:
    print(answer)
