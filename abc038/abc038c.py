N = int(input())
numbers = list(map(int, input().split()))

left = 0
right = 1
count = 0
#print(numbers)
for left in range(N):
    #rightを一個進めたものが条件を満たすか?
    #半開区間で考える
    #print("left:", left)
    #print(numbers[left], numbers[right - 1])
    while right < N and (right <= left or numbers[right - 1] < numbers[right]):
        #print("left:", left, "right:", right)
        #print(numbers[right - 1], numbers[right])
        right += 1
    count += right - left
    #print("updated right:", right)
    #print("count:", count)
    if right == left:
        right += 1

print(count)
