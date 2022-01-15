a, b, c = map(int, input().split())

if a == b == c:
    print(0)
else:
    if a >= b and a >= c:
        print('A', end=' ')
    if b >= a and b >= c:
        print('B', end=' ')
    if c >= a and c >= b:
        print('C', end=' ')
