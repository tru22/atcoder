inputLine = list(str(input()))
a, b = str(input()).split(' ')
a = int(a)
b = int(b)

charA = inputLine[a - 1]
charB = inputLine[b - 1]

inputLine[a - 1] = charB
inputLine[b - 1] = charA

print(''.join(inputLine))
