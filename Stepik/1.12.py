a = list(map(int, input().split()))
if len(a) == 1:
    print(*a)
else:
    b = [0] * len(a)
    for i in range(len(a) - 1):
        b[i] = a[i - 1] + a[i + 1]
    b[-1] = a[0] + a[-2]
    print(*b)
