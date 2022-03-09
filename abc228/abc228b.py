N, X = map(int, input().split())
friends = list(map(int, input().split()))

#print("friends: ", friends)

idx = X
knownFriends = [X]
count = 0
for i in range(N):
    #print(idx, knownFriends, friends[idx - 1])
    knownFriends.append(friends[idx - 1])
    idx = friends[idx - 1]

print(knownFriends)
print(len(set(knownFriends)))
