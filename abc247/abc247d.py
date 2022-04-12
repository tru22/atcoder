Q = int(input())
queue = []

for i in range(Q):
    queries = list(map(int, input().split()))
    #print(queue)
    if len(queries) == 3:
        queue.append([queries[1], queries[2]]) #number x, c times
    elif len(queries) == 2:
        partition = queries[1]
        summation = 0
        while partition != 0:
            if queue[0][1] > partition:
                summation += queue[0][0] * partition
                queue[0][1] = queue[0][1] - partition
                partition = 0
            else:
                summation += queue[0][0] * queue[0][1]
                partition = partition - queue[0][1]
                queue.pop(0)
        print(summation)
