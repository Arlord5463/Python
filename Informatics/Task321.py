n = int(input())
summa = 1
for i in range(1, n + 1):
    summa += (-1) ** i / (2 * i + 1)
print(summa * 4)
