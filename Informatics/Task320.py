n = int(input())
g = 1
for i in range(2, n + 1):
    g += (1 / (i ** 2))
print(g)
