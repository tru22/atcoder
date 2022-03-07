N = int(input())
maxlen = 3

if N >= 42:
    print("AGC" + "".join(["0" for i in range(maxlen - len(str(N)))]) + str(N + 1))
else:
    print("AGC" + "".join(["0" for i in range(maxlen - len(str(N)))]) + str(N))
