a, b, c = map(int, input().split())
numbers = sorted([a, b, c])

if numbers[1] == b:
    print("Yes")
else:
    print("No")
