N = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse = True)

sumAlice = 0
sumBob = 0
for i in range(len(cards)):
    if (i + 1) % 2 == 1:
        sumAlice += cards[i]
    else:
        sumBob += cards[i]
print(sumAlice - sumBob)
