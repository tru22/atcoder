N = int(input())
inputLine = str(input()).split(' ')
inputLine = list(map(int, inputLine))

originalSum = 4 * sum([i + 1 for i in range(N)])
currentSum = sum(inputLine)

print(originalSum - currentSum)
