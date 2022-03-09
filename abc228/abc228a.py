S, T, X = map(int, input().split()) #つける時間, 消す時間, ターゲット

if T < S: #消す時間がつける時間より小さい = 0時を跨ぐ
    if (S <= X and X <= 23) or (0 <= X  and X < T):
        print("Yes")
    else:
        print("No")
else: #消す時間がつける時間より大きい = 0時を跨がない
    if S <= X and X < T:
        print("Yes")
    else:
        print("No")
