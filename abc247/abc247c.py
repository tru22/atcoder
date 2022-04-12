N = int(input())

def sequence(N):
    if N > 1:
        return sequence(N - 1) + " " + str(N) + " " + sequence(N - 1)
    else:
        return "1"

print(sequence(N))
