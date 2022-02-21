count = 0
n = 1
while n <= 2020:
    d = 2020 % n
    n += 1
    if d == 22:
        count += 1
        print(n-1)

print(count)
