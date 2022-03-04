L, R = map(int, input().split())
sentence = input()

pre = sentence[:L - 1]
mid = sentence[L - 1:R]
suf = sentence[R:]
print(pre + mid[::-1] + suf)
