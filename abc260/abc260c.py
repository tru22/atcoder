# global
n, x, y = map(int, input().split())

reds = [0 for i in range(10)]
blues = [0 for i in range(10)]

reds[n - 1] = 1

def exchange(reds, blues):
    flagA = False
    for i in range(1, len(reds)):
        # level = i + 1
        if reds[i] > 0:
            flagA = True
            tmplevel = i
            blues[tmplevel] += reds[tmplevel] * x
            reds[tmplevel - 1] += reds[tmplevel]
            reds[tmplevel] = 0
            #print("a---")
            #print(reds, blues)
        else:
            continue

    flagB = False
    for i in range(1, len(blues)):
        if blues[i] > 0:
            flagB = True
            tmplevel = i
            blues[tmplevel - 1] += blues[tmplevel] * y
            reds[tmplevel - 1] += blues[tmplevel]
            blues[tmplevel] = 0
            #print("a---")
            #print(reds, blues)
        else:
            continue

    if flagA == False and flagB == False:
        return reds, blues
    else:
        return exchange(reds, blues)

reds, blues = exchange(reds, blues)
print(blues[0])
