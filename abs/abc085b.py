N = int(input())
radiusList = []
for i in range(N):
    radiusList.append(int(input()))
radiusList.sort(reverse = True)

count = 0
formRad = 101
for i in range(len(radiusList)):
    if formRad > radiusList[i]:
        count += 1
        formRad = radiusList[i]
print(count)
