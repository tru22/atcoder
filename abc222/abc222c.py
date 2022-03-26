N, M = map(int, input().split())

def match(act1, act2):
    if act1 == act2:
        return 0, 0
    elif act1 == "P" and act2 == "G" or act1 == "C" and act2 == "P" or act1 == "G" and act2 == "C":
        return 1, 0
    elif act1 == "G" and act2 == "P" or act1 == "P" and act2 == "C" or act1 == "C" and act2 == "G":
        return 0, 1

actions = []
for i in range(2 * N):
    actions.append(list(input()))

people = [[i + 1, 0] for i in range(2 * N)] #number, score

#print(people, actions)
for i in range(M):
    for j in range(0, 2 * N, 2):
        idx1 = people[j][0] - 1
        idx2 = people[j + 1][0] - 1
        s1, s2 = match(actions[idx1][i], actions[idx2][i])
        people[j][1] += s1
        people[j + 1][1] += s2
    people.sort(key = lambda x: (x[1], x[1] - x[0]))
    #print(people)

people.sort(key = lambda x: (x[1], x[1] - x[0]))
people = people[::-1]
for i in range(len(people)):
    print(people[i][0])
#print(people)
