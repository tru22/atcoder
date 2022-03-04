#素直に全探索を書くのが一番はやい
#即ち(A+1)(B+1)(C+1)
#三重ループでも，制約条件により計算量にして10^5回くらい
A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            if 500 * i + 100 * j + 50 * k == X:
                count += 1
print(count)
