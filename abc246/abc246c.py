N, K, X = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort(reverse = True)

def discount(price, coupon):
    if price - coupon >= 0:
        return price % coupon, price // coupon #changedprice, usedcoupons
    else:
        return 0, 1

used = 0
i = 0
j = 0
while used < K:
    if prices[i] >= X or j >= 1:
        changedtmp, usedtmp = discount(prices[i], X)
        used += usedtmp
        if used > K:
            prices[i] = prices[i] - (K - (used - usedtmp)) * X
            break
        else:
            prices[i] = changedtmp
    i += 1
    print(prices, used)
    if i > N - 1:
        j += 1
        i = 0
        prices.sort(reverse = True)

print(prices)
print(sum(prices))
