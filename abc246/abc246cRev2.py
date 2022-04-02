N, K, X = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort(reverse = True)

def discount(price, coupon):
    if price - coupon >= 0:
        return price % coupon, price // coupon #changedprice, usedcoupons
    else:
        return 0, 1

print([i % X for i in prices])
print([i // X for i in prices])
print(prices)

rems = [i % X for i in prices]
mods = [i // X for i in prices]

summation = 0
used = 0
if sum(mods) > K:
    i = 0
    while used <= K:
        summation += rems[i]
        used += mods[i]
        i += 1
    print(summation)

else:
    i = 0
    used = sum(mods)    
    rems.sort(reverse = True)
    while used <= K and i < N:
        used += 1 + mods[i]
        rems[i] = 0
        i += 1
    print(rems)
    print(sum(rems))
