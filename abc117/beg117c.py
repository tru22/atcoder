inputLine = str(input()).split(' ')
N = int(inputLine[0])
M = int(inputLine[1])
     
objectives = str(input()).split(' ')
objectives = list(map(int, objectives))
objectives.sort()
#print(objectives)
     
offsets = []
if len(objectives) == 1 or (N - M >= 0):
    print('0')
    exit()
        
for i in range(len(objectives) - 1):
    diff = (objectives[i + 1] - objectives[i], i + 1)
    offsets.append(diff)
#print(offsets)
     
offsets = sorted(offsets, key = lambda x : x[0], reverse = True)
#print(offsets)
     
markers = [0] #add a start
for i in range(N - 1):
    markers.append(offsets[i][1])
    markers.append(len(objectives)) #add a goal
    #print(markers)
     
movement = 0
for j in range(len(markers) - 1):
    movement += objectives[markers[j + 1] - 1] - objectives[markers[j]]
print(movement)
