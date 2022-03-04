number = list(input())
#a, b, c = map(int, number)
#print(a, b, c)

num1 = int("".join(number))
num2 = int("".join([number[1], number[2], number[0]]))
num3 = int("".join([number[2], number[0], number[1]]))

print(num1 + num2 + num3)
