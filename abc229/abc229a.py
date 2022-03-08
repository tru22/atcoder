fields = []
count = []

for i in range(2):
    current = list(input())
    count.append(sum([1 for i in current if i == "#"]))
    fields.append(current)



if count[0] + count[1] == 2:
    if count[0] == 2 or count[1] == 2:
        print('Yes')
    else:
        if fields[0][0] == fields[1][0]:
            print('Yes')
        else:
            print('No')
else:
    print('Yes')
