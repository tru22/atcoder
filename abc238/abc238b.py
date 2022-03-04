columnNum = int(input())
angles = list(map(int, input().split()))
#print(angles)
anglesMod = [0, 360]
summation = 0
for i in range(len(angles)):
    summation += angles[i]
    anglesMod.append(summation % 360)
anglesMod.sort()
#print(anglesMod)

maximum = 0
for i in range(len(anglesMod) - 1):
    if anglesMod[i + 1] - anglesMod[i] > maximum:
        maximum = anglesMod[i + 1] - anglesMod[i]

print(maximum)
