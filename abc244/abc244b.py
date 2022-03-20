N = int(input())
T = list(input())

position = [0, 0]
direction = 0 #0, 1, 2, 3 東 北 西 南
for i in range(N):
    if T[i] == "S":
        if direction == 0:
            position[0] += 1
        elif direction == 1:
            position[1] += 1
        elif direction == 2:
            position[0] -= 1
        elif direction == 3:
            position[1] -= 1
    else:
        if direction == 0:
            direction = 3
        elif direction == 1:
            direction = 0
        elif direction == 2:
            direction = 1
        elif direction == 3:
            direction = 2
    #print(direction)

print(position[0], position[1])
