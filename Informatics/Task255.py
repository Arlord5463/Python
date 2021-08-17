n = int(input())
c = int(1)
for i in range(1, n):
    for j in range(i):
        if c > n:
            break
        print(i, end='')
        c += 1
